#!usr/bin/python3
"""issubclass"""
def inherits_from(obj, a_class):
    """wowowo
    Args:
        obj (any): the ibject
        a_class (type): the tyepkedf
    Returns:
        True or False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False