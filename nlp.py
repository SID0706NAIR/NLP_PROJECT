import pyttsx3
import speech_recognition as sr

def main():
    print("NLP Accessibility Tool active. Choose an option.")

    while True:
        print("\n" + "="*40)
        print("1. Real-time Speech-to-Text (Accessibility Mode)")
        print("2. Text-to-Speech (Screen Reader Mode)")
        print("3. Exit Program")
        print("="*40)
        
        choice = input("Select (1-3): ")

        if choice == '1':
            # Option 1: Speech-to-Text
            recognizer = sr.Recognizer()
            # Adjust for ambient noise to improve search accuracy
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("\n[System]: Listening... Speak now.")
                try:
                    audio = recognizer.listen(source, timeout=5)
                    print("[System]: Processing voice...")
                    # Uses Google's pre-trained model (Search-based decoding)
                    text = recognizer.recognize_google(audio)
                    print(f"[Output]: You said: {text}")
                except sr.UnknownValueError:
                    print("[Error]: Could not understand audio.")
                except sr.RequestError:
                    print("[Error]: Service unreachable.")
                except Exception as e:
                    print(f"[Error]: {e}")

        elif choice == '2':
            # Option 2: Text-to-Speech 
            # Initializing inside the choice block prevents the "second-run hang"
            text_to_read = input("Enter the text you want the assistant to read: ")
            
            if text_to_read.strip():
                print(f"\n[Output]: Reading aloud...")
                
                # Create a fresh engine instance for this specific speech task
                engine = pyttsx3.init()
                engine.setProperty('rate', 170)
                engine.setProperty('volume', 1.0)
                
                engine.say(text_to_read)
                engine.runAndWait()
                
                # Force the engine to stop and clear the audio driver queue
                engine.stop() 
                del engine 
            else:
                print("[Error]: No text entered.")

        elif choice == '3':
            print("Exiting Program. Goodbye!")
            break
        
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")