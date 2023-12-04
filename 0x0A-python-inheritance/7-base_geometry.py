#!/usr/bin/python3
"""Let's write a basic empty basegemotery"""
class BaseGeometry:
    """the base"""
    def area(self):
        """not yet"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates integer
        Args:
            name (str): the name of the parameter
            value (int): the value
        Raises:
            TypeError if not int
            ValueError if < 0 """
        if (isinstance(value, int) == False):
            raise TypeError("{} must be an integer".format(name))
        if (value < 0):
            raise ValueError("{} must be greater than 0".format(name))