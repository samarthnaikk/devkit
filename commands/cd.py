import os
import sys

def run(args):
    if len(args) != 1:
        print("Usage: devkit cd <directory>")
        sys.exit(1)
    
    target_dir = args[0]
    
    try:
        os.chdir(target_dir)
        print(f"Changed directory to {os.getcwd()}")
    except FileNotFoundError:
        print(f"Error: Directory '{target_dir}' not found.")
