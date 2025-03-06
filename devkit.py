#!/Users/samarthnaik/Desktop/SIA/bin/python
<<<<<<< Updated upstream
=======



>>>>>>> Stashed changes
import sys
import subprocess
from commands import (
    branchmind, commitgen, devfocus, docklight, edit,
    git_simplify, search_web, search, talk, testgen
)

def main():
    if len(sys.argv) < 2:
        print("Usage: devkit <command> [arguments]")
        print("Available commands: branchmind, commitgen, devfocus, docklight, edit, git_simplify, search_web, search, talk, testgen")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    command_map = {
        "branchmind": branchmind.run,
        "commitgen": commitgen.run,
        "devfocus": devfocus.run,
        "docklight": docklight.run,
        "edit": edit.run,
        "git_simplify": git_simplify.run,
        "search_web": search_web.run,
        "search": search.run,
        "talk": talk.run,
        "testgen": testgen.run
    }

    if command in command_map:
        command_map[command](args)
    else:
        print(f"Error: Unknown command '{command}'")
        sys.exit(1)

if __name__ == "__main__":
    main()
