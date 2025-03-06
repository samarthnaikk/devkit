import subprocess
import sys

def run(args):
    if len(args) != 1:
        print("Usage: devkit debug <filename>")
        sys.exit(1)

    filename = args[0]
    
    if filename.endswith(".py"):
        run_python_debugger(filename)
    elif filename.endswith(".c"):
        run_c_debugger(filename)
    else:
        print("Unsupported file type for debugging.")

def run_python_debugger(filename):
    result = subprocess.run(["python3", "-m", "py_compile", filename], capture_output=True, text=True)
    if result.stderr:
        print(f"Errors found:\n{result.stderr}")
    else:
        print("No syntax errors found.")

def run_c_debugger(filename):
    result = subprocess.run(["gcc", "-o", "output", filename], capture_output=True, text=True)
    if result.stderr:
        print(f"Errors found:\n{result.stderr}")
    else:
        print("No compilation errors found.")
