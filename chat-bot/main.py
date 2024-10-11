from complex_reasoning import chat_with_olama
from face_recognition import run_facial_recognition
from speech_to_text import run_speech_to_text
from text_to_speech import run_text_to_speech


context = "";

def main():
    print("Running facial recognition...")
    run_facial_recognition()
    print("Facial recognition completed!")
    
    run_text_to_speech("Hello, I am Chatbot, your personal assistant. How can I help you today?")
    
    
    while True: 
        global context
        prompt = run_speech_to_text()
        logical_response = chat_with_olama(context, prompt)
        run_text_to_speech(logical_response)
        context = f"\nUser: {prompt}\nAI: {logical_response}\n"
        
        
        
        
if __name__ == "__main__":
    main()