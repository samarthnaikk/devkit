import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def run(args):
    print("Welcome to Devkit AI Chat! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = genai.generate_text(user_input)
        print("AI:", response.text)
