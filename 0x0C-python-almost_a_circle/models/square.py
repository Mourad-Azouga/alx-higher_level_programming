#!/usr/bin/python3
"""Let's make a square!"""
from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size, x = 0, y = 0, id = None):
        """This method initializes the square with the same parameters of the Rectangle
        Args:
            size (int) : the size
            x (int) : x coord
            y (int) : y corrd
            id (int) : id"""
        super().__init__(size, size, x, y, id)
    @property
    def size(self):
        """gets the size and sets it"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """Updates the squares with a set of args:
        Args:
            1st (int): ID
            2nd (int): size
            3rd (int): x
            4th (int): y
        """
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
                        self.size = arg
                    case 2:
                        self.x = arg
                    case 3:
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
                    case "size":
                        self.width = val
                    case "x":
                        self.x = val
                    case "y":
                        self.y = val            
    def to_dictionary(self):
         """Rerturns dict rep os the square"""
         return { "id": self.id, "size" : self.width, "x" : self.x, "y" : self.y}