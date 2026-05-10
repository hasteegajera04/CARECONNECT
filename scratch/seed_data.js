
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getFirestore, collection, addDoc, doc, setDoc } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyBj49uFVAdSG1jbELVIdYY6KvG0b8fECiQ",
  authDomain: "new-careconnect.firebaseapp.com",
  projectId: "new-careconnect",
  storageBucket: "new-careconnect.firebasestorage.app",
  messagingSenderId: "7797461074",
  appId: "1:7797461074:web:4a0cd6b23320620a27cf8b",
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

async function seedData() {
  console.log("Seeding CareConnect sample data...");

  // 1. Seed Nurses
  const nurses = [
    {
      name: "Dr. Sarah Johnson",
      role: "nurse",
      specialty: "Geriatric Care",
      experience: "10 Years",
      location: "New York, NY",
      rating: 4.9,
      bio: "Specializing in post-operative care and elderly support.",
      email: "sarah.j@example.com",
      phone: "+1 234 567 8901",
      image: "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&q=80&w=2070"
    },
    {
      name: "Nurse David Chen",
      role: "nurse",
      specialty: "Critical Care",
      experience: "8 Years",
      location: "San Francisco, CA",
      rating: 4.8,
      bio: "Expert in ICU transition care and vital monitoring.",
      email: "david.c@example.com",
      phone: "+1 345 678 9012",
      image: "https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&q=80&w=2070"
    },
    {
      name: "Emily Rodriguez",
      role: "nurse",
      specialty: "Pediatric Care",
      experience: "5 Years",
      location: "Austin, TX",
      rating: 4.7,
      bio: "Providing compassionate care for families and children.",
      email: "emily.r@example.com",
      phone: "+1 456 789 0123",
      image: "https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&q=80&w=2070"
    }
  ];

  for (const nurse of nurses) {
    try {
      // Use a consistent ID for the demo if needed, or addDoc for new ones
      await addDoc(collection(db, "users"), {
        ...nurse,
        createdAt: new Date()
      });
      console.log(`Added Nurse: ${nurse.name}`);
    } catch (e) {
      console.error("Error adding nurse: ", e);
    }
  }

  console.log("Data seeding complete!");
}

seedData();
