import subprocess

def run(args):
    try:
        result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
        print("Running Docker Containers:\n", result.stdout)
    except Exception as e:
        print(f"Error: {e}")
