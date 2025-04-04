from core.speech_recognition import listen
from core.text_to_speech import speak
from core.command_processor import process_command

def main():
    speak("Hello Animesh! Say 'Hey buddy' to activate me.")

    # Wake word required only once
    while True:
        wake_word = listen()
        if wake_word and "hey buddy" in wake_word.lower():
            speak("I'm activated! Now, just say your command.")
            break
        else:
            print("Waiting for activation...")

    # Continuous command listening (no wake word needed again)
    while True:
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
