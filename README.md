# 🏥 CareConnect - Modern Nurse-Patient Care Platform

CareConnect is a comprehensive healthcare management system designed to bridge the gap between patients and nursing staff. It provide real-time vitals monitoring, AI-driven health risk assessments, and a seamless communication layer for home care and hospital environments.

---

## 🌟 Key Features

### 👩‍⚕️ For Nurses
- **Dynamic Dashboard**: Track assigned patients, upcoming tasks, and urgent alerts.
- **Vitals Logger**: Log and monitor patient vitals (BP, Blood Sugar, SpO2) with real-time updates.
- **Care Info Store**: Maintain detailed logs of food intake, patient complaints, and medication schedules.
- **Patient Management**: View detailed medical histories and risk profiles of assigned patients.

### 👤 For Patients
- **Health Snapshot**: View real-time health data and monitoring status.
- **Nurse Connection**: Request professional nursing assistance and track request status.
- **Vitals History**: Access historical trends of vital signs in an intuitive interface.
- **AI Health Assistant**: Integrated Gemini-powered AI to answer health-related queries and provide preliminary advice.

### 🧠 Smart Features
- **AI Risk Assessment**: Automated calculation of health risks based on medical vitals.
- **Real-time Sync**: Powered by Firebase Firestore for instantaneous data updates across all portals.
- **Responsive Design**: Clean, modern UI optimized for both desktop and mobile views.

---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | HTML5, Vanilla CSS3, JavaScript (ES6+) |
| **Backend** | Python, Flask |
| **Database** | Firebase Firestore |
| **Authentication** | Firebase Auth |
| **AI Integration** | Google Gemini API |

---

## 📂 Project Structure

```text
CareConnect/
├── backend/            # Flask Server
│   ├── app.py          # Application Entry Point
│   ├── routes.py       # API Endpoints (Risk Calc, AI Chat)
│   ├── service.py      # Business Logic & AI Integration
│   └── requirements.txt
├── frontend/           # Web Interface
│   ├── firebase.js     # Firebase Configuration
│   ├── login.html      # Authentication
│   ├── nurse-*.html    # Nurse Portal Pages
│   └── patient-*.html  # Patient Portal Pages
├── scratch/            # Development Utility Scripts
└── DEMO_CREDENTIALS.md # Test Accounts
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js (for optional frontend tooling)
- Firebase Account & Project

### Backend Setup
1. Navigate to the backend folder:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your `.env` file with your Gemini API key.
4. Run the server:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Configure your Firebase credentials in `frontend/firebase.js`.
2. Open `frontend/login.html` in your browser or serve it using a local development server (like Live Server in VS Code).

---

## 🧪 Demo Credentials

For testing purposes, you can use the following pre-configured accounts:

| Role | Email | Password |
| :--- | :--- | :--- |
| **Patient** | `ramesh@gmail.com` | `123456` |
| **Nurse** | `nancy@gmail.com` | `123456` |

---

## 📄 License
This project is for educational and presentation purposes.

---
*Built with ❤️ for a better healthcare experience.*
