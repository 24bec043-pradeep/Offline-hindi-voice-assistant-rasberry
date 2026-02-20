mport os
import sys
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json
import subprocess
import time

# --- UNICODE KEYWORDS (Nano Friendly) ---
WAKE_WORD = "\u0928\u092e\u0938\u094d\u0924\u0947" # ?????? (Namaste)
KAISE = "\u0915\u0948\u0938\u0947"             # ???? (Kaise)
NAAM = "\u0928\u093e\u092e"                 # ??? (Naam)
SAMAY = "\u0938\u092e\u092f"                # ??? (Samay)
BAND = "\u092c\u0902\u0926"                  # ??? (Band)

q = queue.Queue()

def speak_offline(text):
    """Bina internet ke bolne ke liye (espeak-ng)"""
    print(f"Assistant: {text}")
    # Voice: Hindi (-v hi), Speed: 140 (-s 140)
    try:
        subprocess.call(['espeak-ng', '-v', 'hi', '-s', '150', '-p', '50', text])
        time.sleep(0.3) 
        
        with q.mutex:
            q.queue.clear()
    except Exception as e:
        print(f"Speaker error: {e}")

def callback(indata, frames, time, status):
    if status:
        
        pass 
    q.put(bytes(indata))

# --- Model Loading ---
if not os.path.exists("model"):
    print("Error: 'model' folder nahi mila! Please check karein.")
    exit(1)

model = Model("model")
fs = 44100
rec = KaldiRecognizer(model, fs)

is_active = False 



print("\n--- ASSISTANT TAIYAAR HAI ---")
print("Boliye: 'Namaste' shuru karne ke liye...")

try:
    
    with sd.RawInputStream(samplerate=fs, blocksize=16000, dtype='int16',
                           channels=1, callback=callback):

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")

                if text:
                    print(f"Suna gaya: {text}")

                    # --- Condition 1: Wake Word Detection ---
                    if not is_active:
                        if WAKE_WORD in text:
                            is_active = True
                            speak_offline("Ji, main sun raha hoon. Boliye?")
                        continue

                    # --- Condition 2: Active Mode Commands ---
                    if is_active:
                        if KAISE in text:
                            speak_offline("Main bilkul thik hoon, shukriya.")

                        elif NAAM in text:
                            speak_offline("Mera naam Raspberry Assistant hai.")

                        elif SAMAY in text:
                            current_time = time.strftime("%I bajkar %M minute")
                            speak_offline(f"Abhi {current_time} ho rahe hain")

                        elif BAND in text:
                            speak_offline("Thik hai, main standby mode mein jaa raha hoon.")
                            is_active = False
                            print("\n--- STANDBY MODE (Namaste ka intezaar hai) ---")

                        else:
                            # Agar command match na ho toh console par dikhaye
                            print("Command match nahi hui.")

except KeyboardInterrupt:
    print("\nProgram band ho raha hai...")
except Exception as e:
    print(f"\nMain Error: {e}")

