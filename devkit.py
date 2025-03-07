#!your-python-dir

import sys
from commands import (
    branchmind, cd, commitgen, convert, debug, devfocus,
    docgen, docklight, edit, explain, git_simplify, make,
    search_web, search, talk, testgen
)

COMMANDS = {
    "branchmind": branchmind.run,
    "cd": cd.run,
    "commitgen": commitgen.run,
    "convert": convert.run,
    "debug": debug.run,
    "devfocus": devfocus.run,
    "docgen": docgen.run,
    "docklight": docklight.run,
    "edit": edit.run,
    "explain": explain.run,
    "git_simplify": git_simplify.run,
    "make": make.run,
    "search_web": search_web.run,
    "search": search.run,
    "talk": talk.run,
    "testgen": testgen.run,
}

def main():
    if len(sys.argv) < 2:
        print("Usage: devkit <command> [args...]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    if command in COMMANDS:
        COMMANDS[command](args)
    else:
        print(f"Error: Unknown command '{command}'")

if __name__ == "__main__":
    main()
