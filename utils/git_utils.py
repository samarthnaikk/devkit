import subprocess

def run_git_command(command):
    try:
        result = subprocess.run(["git"] + command.split(), capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Git Error: {e}"
