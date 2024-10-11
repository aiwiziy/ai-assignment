import speech_recognition as sr



def run_speech_to_text():
    recognizer = sr.Recognizer()
    
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source)
            
            try:
                print("Recognizing...")
                text = recognizer.recognize_google(audio, language='en-NG')
                text = text.lower()
                print("You said: ", text)
                return text
            except Exception as e:
                print("Error: ", str(e))
                k_text = input("Use keyboard to type: ")
                return k_text