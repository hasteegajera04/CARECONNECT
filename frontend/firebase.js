// firebase.js

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyBj49uFVAdSG1jbELVIdYY6KvG0b8fECiQ",
  authDomain: "new-careconnect.firebaseapp.com",
  projectId: "new-careconnect",
  storageBucket: "new-careconnect.firebasestorage.app",
  messagingSenderId: "7797461074",
  appId: "1:7797461074:web:4a0cd6b23320620a27cf8b",
  measurementId: "G-NW9ESBQQQL"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const db = getFirestore(app);
