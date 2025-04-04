import os
import webbrowser
import pyautogui
from core.text_to_speech import speak
from modules.fun_responses import tell_joke, tell_fun_fact
from core.ai_chat import get_ai_response
from core.text_to_speech import speak
from core.speech_recognition import listen  # Import listen function


# Command-action mapping for faster execution
COMMANDS = {
    "open notepad": lambda: (speak("Opening Notepad"), os.system("notepad.exe")),
    "open spotify": lambda: (speak("Opening Spotify"), os.system("C:\Program Files\BraveSoftware\Brave-Browser\Application")),
    "open chat gpt": lambda: (speak("Opening ChatGPT, choom!"), webbrowser.open("https://chat.openai.com")),
    "open openai": lambda: (speak("Opening ChatGPT, choom!"), webbrowser.open("https://chat.openai.com")),
    "open open ai": lambda: (speak("Opening ChatGPT, choom!"), webbrowser.open("https://chat.openai.com")),
    "tell me a joke": lambda: (speak("Alright! Here's a joke for you."), tell_joke()),
    "tell me a fun fact": lambda: (speak("Here's an interesting fact!"), tell_fun_fact()),
    "give me a fun fact": lambda: (speak("Here's an interesting fact!"), tell_fun_fact()),
    "open browser": lambda: (speak("Opening browser"), webbrowser.open("https://www.google.com")),
    "shutdown": lambda: (speak("Shutting down the system"), os.system("shutdown /s /t 5")),
    "increase volume": lambda: (speak("Increasing volume"), pyautogui.press("volumeup", presses=5)),
    "decrease volume": lambda: (speak("Decreasing volume"), pyautogui.press("volumedown", presses=5)),
    "exit": lambda: (speak("Goodbye! buddy take care!"), exit()),
    "stop": lambda: (speak("Goodbye!"), exit())
}
def chat_mode():
    """Enters AI chat mode using Gemini 2.0 Flash."""
    speak("Sure! Let's chat. Say 'end chat' to stop.")

    while True:
        user_input = listen()  # Listen to user input
        if user_input.lower() == "end chat":
            speak("Okay! Exiting chat mode.")
            break  # Exit the loop when user says "end chat"

        response = get_ai_response(user_input)  # Get response from Gemini
        speak(response)  # Speak the AI's response

# Update command mapping
COMMANDS["chat with me"] = chat_mode


def process_command(command):
    """Processes user commands and performs actions."""
    command = command.lower().strip()  # Normalize input to lowercase and remove extra spaces
    action = COMMANDS.get(command)

    if action:
        action()  # Execute the mapped function
    else:
        speak("Sorry, I didn't understand that command.")
