#!/usr/bin/python3
"""Let's append a file"""
def append_write(filename="", text=""):
    """This method should do it
    Args:
        filename (FILE): the file that will be appeneded
        text (str): the text that will appened the file
    """
    with open(filename, "a", encoding = "utf-8") as f:
        return f.write(text)