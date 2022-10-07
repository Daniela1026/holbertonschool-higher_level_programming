#!/usr/bin/python3
"""module for Rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    def __init__(self, height=0, width=0):
        """initiation of height and width for a rectangle"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

