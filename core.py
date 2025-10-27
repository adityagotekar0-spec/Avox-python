import speech_recognition as sr

def record_and_recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Say something...")
        audio = r.listen(source)
        print("⏳ Recognizing...")
        try:
            text = r.recognize_google(audio)
            print("✅ You said:", text)
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
        except sr.RequestError as e:
            print(f"⚠️ Could not connect to the service: {e}")

if __name__ == "__main__":
    print("🟢 Avox is starting up...")
    record_and_recognize()
