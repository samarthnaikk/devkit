import google.generativeai as genai
from utils.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def generate_text(prompt):
    try:
        response = genai.generate_text(prompt)
        return response.text
    except Exception as e:
        return f"AI Error: {e}"
