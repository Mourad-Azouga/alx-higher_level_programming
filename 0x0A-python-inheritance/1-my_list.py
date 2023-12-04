#!/usr/bin/python3
"""Write a class MyList that inherits from list"""
class MyList(list):
    """This should do it"""
    def print_sorted(self):
        """as well as this"""
        return (sorted(self))
