#!/usr/bin/python3
"""let's read an object to a file using json"""
import json
def load_to_json_file(filename):
    """This function does that
    Args:
        filename (file): the file we'll fileing intio
    """
    with open(filename, "r") as f:
        return json.load(f)