import google.generativeai as genai
from config import GEMINI_API_KEY
import sys

genai.configure(api_key=GEMINI_API_KEY)

def run(args):
    if len(args) < 3:
        print("Usage: devkit make <language> <output_file> <description>")
        sys.exit(1)

    language = args[0]
    output_file = args[1]
    description = " ".join(args[2:])

    prompt = f"Write a {language} program that {description}"

    response = genai.generate_text(prompt)
    
    with open(output_file, "w") as f:
        f.write(response.text)

    print(f"Generated {language} code in {output_file}")
