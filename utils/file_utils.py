import os

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return None

def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
