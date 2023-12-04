#!/usr/bin/python3
"""Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False."""
def is_same_class(obj, a_class):
    """Check if obj is in a class
    Args:
        obj: object to
        a_class (type): the type
    Return:
        1 if there is, 0 if not0"""
    if (type(obj) == a_class):
        return True
    else:
        return False