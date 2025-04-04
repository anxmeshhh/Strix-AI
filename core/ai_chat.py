import os
import google.generativeai as genai
from dotenv import load_dotenv
from core.text_to_speech import speak  # So Strix can speak the responses

# Load API key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def chat_with_gemini(prompt):
    """Get response from Google Gemini 2.0 Flash."""
    response = model.generate_content(prompt)
    return response.text.strip() if response.text else "I couldn't generate a response."

def get_ai_response(prompt):
    """Fetch AI response using Gemini."""
    return chat_with_gemini(prompt)
