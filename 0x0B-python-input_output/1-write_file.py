#!/usr/bin/python3
"""Let's write in a file"""
def write_file(filename="", text=""):
    """this method will take care of that
    Args:
        filename (FILE): The file we'll write in
        text (str): the string that will be written inside the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)