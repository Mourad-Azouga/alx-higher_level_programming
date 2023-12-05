#!/usr/bin/python3
"""let's write an object to a file using json"""
import json
def save_to_json_file(my_obj, filename):
    """This function does that
    Args:
        my_obj (object): the object we'll write
        filename (file): the file we'll fileing intio
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)