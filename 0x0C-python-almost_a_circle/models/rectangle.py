#!/usr/bin/python3
"""Let's make a rectangle class"""
from models.base import Base
class Rectangle(Base):
    """Let's make a Rectangle"""
    def __init__(self, width, height, x = 0, y = 0, id = None):
        """This function will initialize the Rectangle
        Args:
            width (int) = width
            height (int) = height
            x (int) = x axis 
            y (int) = y axis
            id (int) = the id"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets the width with a value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    @property
    def height(self):
        """height getter"""
        return self.__height
    @height.setter
    def height(self, value):
        """sets the height with value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    @property
    def x(self):
        """Sets x position"""
        return self.__x
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value
    @property
    def y(self):
        """sets y position"""
        return self.__y
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value
    
    def area(self):
        """This method returns the area of the Rectangle"""
        return self.height * self.width
    
    def display(self):
        """This method returns prints the rectangle using # characters"""
        if self.height == 0 or self.width == 0:
            print("")
            return
        for whitespace in range(self.y):
            print("")
        for i in range(self.height):
            for white in range(self.x):
                print(" ", end ="")
            for j in range(self.width):
                print("#", end = "")
            print("")

    def __str__(self):
        return f"[Rectangle] ({id(self)}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def update(self, *args, **kwargs):
        """This updates the class assigning an arg to each attribute
        Args:
            1st (int) : ID
            2nd (int) : width
            3rd (int) : height
            4th (int) : x
            5th (int) : y
        There is a **kwargs now
        """
        #Here we'll use args
        if args and len(args) != 0:
            counter = 0
            for arg in args:
                match counter:
                    case 0:
                        if arg is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id = arg
                    case 1:
                        self.width = arg
                    case 2:
                        self.height = arg
                    case 3:
                        self.x = arg
                    case 4:
                        self.y = arg
                counter += 1
        #Here we'll use kwargs
        elif kwargs and len(kwargs) != 0:#If the args don't exist but the kwargs do exist
            for key, val in kwargs.items():
                match key:
                    case "id":
                        if val is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id = val
                    case "width":
                        self.width = val
                    case "height":
                        self.height = val
                    case "x":
                        self.x = val
                    case "y":
                        self.y = val            
    def to_dictionary(self):
        """Returns the dictionary rep of the Rectangle"""
        return {"id": self.id, "width" : self.width, "height": self.height, "x": self.x, "y" : self.y}