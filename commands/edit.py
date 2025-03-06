import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def run(args):
    if len(args) < 2:
        print("Usage: devkit edit <filename> <change description>")
        return
    
    filename = args[0]
    change_request = " ".join(args[1:])

    try:
        with open(filename, "r") as f:
            code = f.read()

        prompt = f"Modify this code according to the request:\n{code}\n\nChange request: {change_request}"
        response = genai.generate_text(prompt)

        with open(filename, "w") as f:
            f.write(response.text)

        print(f"File {filename} updated successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
