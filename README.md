# 🎙️ Offline Hindi Voice Assistant (Raspberry Pi)

Ye ek pure **Offline Hindi/Hinglish Voice Assistant** hai jo Raspberry Pi par chalta hai. Isme internet ki zaroorat nahi hai, ye **Vosk** (Speech-to-Text) aur **eSpeak-ng** (Text-to-Speech) ka use karta hai.



## ✨ Features
- **100% Offline:** Aapki voice data secure hai, internet ki zaroorat nahi.
- **Wake Word:** "Namaste" bolne par hi active hota hai.
- **Hinglish Support:** Hindi aur English dono samajhta hai.
- **Low Latency:** Raspberry Pi 4/5 par bahut fast response deta hai.

## 🛠️ Requirements
- Raspberry Pi (3, 4, ya 5)
- USB Microphone ya Sound Card
- Speaker (3.5mm jack ya USB)
- Python 3.11+

## 🚀 Installation

1. **System Packages Install karein:**
   ```bash
   sudo apt update
   sudo apt install espeak-ng python3-pip libttspico-utils -y# Offline-hindi-voice-assistant-rasberry
   pip install vosk sounddevice numpy pyttsx3 --break-system-packages

   Vosk Model Download karein:
Vosk ka Hindi model yahan se download karein aur project folder mein model naam se extract karein.

🚦 How to Use
Project folder mein jaein aur script run karein:

Bash
python assistant.py
Assistant standby mode mein rahega.

Boliye: "Namaste"

Assistant bolega: "Ji, main sun raha hoon."

Ab aap commands de sakte hain jaise "Kaise ho?", "Samay kya hai?", ya "Band karo".

📝 Commands List
Wake Word: Namaste (नमस्ते)

Status: Kaise ho? (कैसे हो)

Identity: Tumhara naam kya hai? (नाम)

Time: Samay kya hai? (समय)

Exit: Assistant band karo (बंद)
