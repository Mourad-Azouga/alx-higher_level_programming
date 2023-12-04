#!/usr/bin/python
"""function that returns True if the object is an instance of
or if the object is an instance of a class that inherited from
the specified class ; otherwise False."""
def is_kind_of_class(obj, a_class):
    """does the stuffies
    Args:
        obj: the object we'll look for
        a_class (type): the place where we'll look for it
    Return:
        True if found
        False if not"""
    if (isinstance(obj, a_class)):
        return True
    return False
