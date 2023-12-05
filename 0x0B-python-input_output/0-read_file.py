#!/usr/bin/python3
"""Let's read a file"""
def read_file(filename=""):
    """This method reads a file 'filename'"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")