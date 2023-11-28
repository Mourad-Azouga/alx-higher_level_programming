#!/usr/bin/python3
"""This is a function that prints stuffies"""

def say_my_name(first_name, last_name=""):
    """This functions does the printing
    Args:
        first_name (string)
        last_name (string)
    
    Raises:
        TypeError: when the names aren't a string
    """
    if not isinstance(first_name, str):
        TypeError ("first_name must be a string")
    if not isinstance(last_name, str):
        TypeError ("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))