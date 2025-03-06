import os

def run(args):
    if len(args) < 1:
        print("Usage: devkit search <filename>")
        return

    filename = args[0]
    for root, _, files in os.walk("."):
        if filename in files:
            print(f"Found: {os.path.join(root, filename)}")
