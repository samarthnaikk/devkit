import google.generativeai as genai
from config import GEMINI_API_KEY
import sys

genai.configure(api_key=GEMINI_API_KEY)

def run(args):
    if len(args) != 1:
        print("Usage: devkit explain <filename>")
        sys.exit(1)

    filename = args[0]

    try:
        with open(filename, "r") as f:
            code = f.read()
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Generate documentation for this code:\n{code}")
        print(response.text)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
