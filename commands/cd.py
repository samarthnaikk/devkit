import os
import sys
import json
from datetime import datetime

HISTORY_FILE = os.path.expanduser("~/.devkit_cd_history.json")
TIME_SLOT_INTERVAL = 1  # Define slot size (1 hour)

def load_history():
    """Load directory history from JSON file."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    """Save directory history to JSON file."""
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)

def get_current_time_slot():
    """Returns the current time slot (e.g., '04-05' for 4-5 AM)."""
    now = datetime.now()
    slot_start = now.hour // TIME_SLOT_INTERVAL * TIME_SLOT_INTERVAL
    slot_end = slot_start + TIME_SLOT_INTERVAL
    return f"{slot_start:02d}-{slot_end:02d}"

def get_most_frequent_directory(history, time_slot=None):
    """Find the most frequent directory, optionally filtered by time slot."""
    freq = {}
    for entry in history:
        path = entry["path"]
        if time_slot:
            entry_time_slot = datetime.fromisoformat(entry["timestamp"]).hour // TIME_SLOT_INTERVAL * TIME_SLOT_INTERVAL
            entry_time_slot_str = f"{entry_time_slot:02d}-{entry_time_slot + TIME_SLOT_INTERVAL:02d}"
            if entry_time_slot_str != time_slot:
                continue  # Skip entries outside this time slot
        freq[path] = freq.get(path, 0) + 1
    return max(freq, key=freq.get, default=None)

def run(args):
    history = load_history()
    now = datetime.now().isoformat()

    if len(args) == 0:
        # Predict most frequent directory based on time slot
        time_slot = get_current_time_slot()
        most_frequent = get_most_frequent_directory(history, time_slot)
        if most_frequent:
            print(most_frequent)  # Print most frequent dir
            return
        print(os.getcwd())  # Default to current dir
        return

    arg = args[0]

    if arg.startswith("-"):
        # Handle `devkit cd -N`
        try:
            steps_back = int(arg)
            if abs(steps_back) > len(history):
                print(os.getcwd())  # No valid history entry
                return
            target_dir = history[steps_back]["path"]
            print(target_dir)  # Print path for shell function
        except (ValueError, IndexError):
            print(os.getcwd())  # Default to current dir on error
        return

    # Regular directory change
    target_dir = os.path.abspath(os.path.expanduser(arg))
    if os.path.isdir(target_dir):
        print(target_dir)  # Print path for shell function

        # Update history
        history.append({"path": target_dir, "timestamp": now})
        if len(history) > 50:  # Keep last 50 entries
            history.pop(0)
        save_history(history)
    else:
        print(os.getcwd())  # Stay in the current directory if invalid
