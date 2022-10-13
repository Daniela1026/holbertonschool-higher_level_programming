#!/usr/bin/python3
"""module square #1"""


Rectangle = __import__('9-rectangle').Rectangle
"""Write a class Square that inherits from Rectangle"""


class Square(Rectangle):
    """init and area """
    def __init__(self, size):
        """ instantiate size """
        super().__init__(size, size)

    def area(self):
        """ Return the area of a square """
        return super().area()
