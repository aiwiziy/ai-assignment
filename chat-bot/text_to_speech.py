import pyttsx3

def run_text_to_speech(text):
    print("Olama: ", text)
    
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(text)

    
    engine.runAndWait()