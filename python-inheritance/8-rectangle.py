#!/usr/bin/python3
"""module rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Write a class Rectangle that inherits from BaseGeometry """


class Rectangle(BaseGeometry):
    """ define init """
    def __init__(self, width, height):
        """ instantiation private width and height """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
