import google.generativeai as genai
from config import GEMINI_API_KEY
import subprocess

genai.configure(api_key=GEMINI_API_KEY)

def run(args):
    try:
        result = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True)
        diff_text = result.stdout

        if not diff_text:
            print("No staged changes to commit.")
            return

        prompt = f"Generate a commit message for these changes:\n{diff_text}"
        response = genai.generate_text(prompt)

        print(f"Suggested Commit Message:\n{response.text}")
    except Exception as e:
        print(f"Error: {e}")
