#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""lets make a square"""

class square(Rectangle):
    def __init__(self, size):
        """
        initializes the square
        Args:
            size (int): should be the size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
