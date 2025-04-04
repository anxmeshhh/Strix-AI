import pyttsx3

# Initialize the TTS engine once (avoids repeated initialization)
engine = pyttsx3.init()

# Set speech properties
engine.setProperty('rate', 200)  # Speed up speech (default ~150)
engine.setProperty('volume', 1.0)  # Max volume

# Optional: Change voice (Index 1 is usually a female voice, 0 is male)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change to voices[1] for another option

def speak(text):
    """Converts text to speech with optimized speed and voice settings."""
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello! I am Strix AI, your fast and efficient assistant.")
