#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """defines the rectangle"""
    def __init__(self, width, height):
        """initializes the rectangle
        Args:
            width (int): width
            height (int): height
        Raises:
            ValueError if <=0
            TypeError if not int
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """this will now defgine the area"""
        return self.__height / self.__width
    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
    