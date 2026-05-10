from datetime import datetime
from typing import Dict, Any, List
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class HealthRiskCalculator:
    """
    Service class responsible for calculating health risks.
    Encapsulates all medical logic.
    """

    def compute_risk(self, vitals: Dict[str, Any]) -> Dict[str, Any]:
        score = 0
        reasons = []

        # Standardized inputs (Clean API Contract)
        sbp = vitals.get('systolic_bp')
        dbp = vitals.get('diastolic_bp')
        sugar = vitals.get('blood_sugar')
        sp02 = vitals.get('oxygen_level')
        hr = vitals.get('heart_rate')
        sleep = vitals.get('sleep_hours', 7)
        prev_score = vitals.get('previous_score')

        # --- LOGIC ENGINE ---
        
        # 1. Hypertension (BP)
        if sbp and dbp:
            if sbp >= 180 or dbp >= 120:
                score += 40
                reasons.append("Critical: Hypertensive Crisis")
            elif sbp >= 140 or dbp >= 90:
                score += 20
                reasons.append("Stage 2 Hypertension")
        
        # 2. Diabetes (Sugar)
        if sugar:
            if sugar > 200:
                score += 30
                reasons.append("Hyperglycemia (High Blood Sugar)")
            elif sugar < 70:
                score += 25
                reasons.append("Hypoglycemia Risk")

        # 3. Hypoxia (Oxygen)
        if sp02:
            if sp02 < 90:
                score += 50
                reasons.append("Critical: Hypoxia (Low Oxygen)")
            elif sp02 < 95:
                score += 15
                reasons.append("Low Oxygen Saturation")

        # 4. Heart Rate
        if hr:
            if hr > 100:
                score += 10
                reasons.append("Tachycardia (High Heart Rate)")
            elif hr < 50:
                score += 10
                reasons.append("Bradycardia (Low Heart Rate)")

        # 5. Lifestyle
        if sleep and sleep < 5:
            score += 5
            reasons.append("Chronic Sleep Deprivation")

        # Cap score
        final_score = min(score, 100)
        
        return {
            "risk_score": final_score,
            "risk_label": self._classify_score(final_score),
            "reasons": reasons if reasons else ["Vitals within normal limits"],
            "trend": self._calculate_trend(final_score, prev_score),
            "calculated_at": datetime.utcnow().isoformat() + "Z"
        }

    def _classify_score(self, score: int) -> str:
        if score < 30: return "Low"
        elif score < 60: return "Medium"
        else: return "High"

    def _calculate_trend(self, current: int, previous: int) -> str:
        if previous is None: return "New"
        diff = current - previous
        if diff > 5: return "Worsening"
        elif diff < -5: return "Improving"
        else: return "Stable"

class GeminiChatService:
    """
    Service class for interacting with OpenRouter AI.
    Provides conversational health feedback using any model.
    """
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.model_name = os.getenv("OPENROUTER_MODEL", "google/gemini-flash-1.5")
        if self.api_key and self.api_key != "YOUR_OPENROUTER_API_KEY_HERE":
            self.enabled = True
        else:
            self.enabled = False

    def get_ai_response(self, user_query: str, vitals_context: Dict[str, Any] = None) -> str:
        if not self.enabled:
            return "AI interaction is currently disabled. Please configure the OPENROUTER_API_KEY in the backend .env file."

        prompt = f"""
        You are a highly professional medical AI assistant for the 'CareConnect' platform. 
        Your goal is to provide helpful, empathetic, and accurate health feedback to patients and caregivers.
        
        Context of current patient vitals:
        {vitals_context if vitals_context else "No vitals data available yet."}
        
        User Question: {user_query}
        
        Guidelines:
        1. Always be professional and empathetic.
        2. If vitals look critical (e.g., BP > 180/120 or SpO2 < 90), strongly advise seeking immediate medical attention.
        3. Do not give specific prescription dosages; suggest consulting a doctor for medication changes.
        4. Keep responses concise and easy to understand for elderly patients.
        5. Use formatting like bullet points if helpful.
        """

        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://careconnect.demo", # Optional
                    "X-Title": "CareConnect AI", # Optional
                },
                data=json.dumps({
                    "model": self.model_name,
                    "messages": [
                        {"role": "user", "content": prompt}
                    ]
                })
            )
            
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            else:
                return f"Error from OpenRouter: {response.text}"
                
        except Exception as e:
            return f"Error communicating with AI: {str(e)}"
