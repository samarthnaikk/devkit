import subprocess

def run(args):
    try:
        result = subprocess.run(["git", "branch", "-a"], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")
