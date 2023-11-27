#!usr/bin/python3
"""def class rectangle"""
class Rectangle:
    """Rectangle"""
    def __init__(self, width = 0, height = 0):
        """init new rectangle.
        Args: 
        width (int):the width
        height (int):the height"""
        self.width = width
        self.height = height
    @property
    def width(self):
        """sets the width"""
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """sets the height"""
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TyperError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
