import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def run(args):
    if len(args) != 1:
        print("Usage: devkit testgen <filename>")
        return

    filename = args[0]

    try:
        with open(filename, "r") as f:
            code = f.read()

        prompt = f"Generate unit tests for the following code:\n{code}"
        response = genai.generate_text(prompt)

        test_filename = f"test_{filename}"
        with open(test_filename, "w") as f:
            f.write(response.text)

        print(f"Generated unit tests in {test_filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
