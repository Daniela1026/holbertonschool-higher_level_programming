#!/usr/bin/python3
"""module square #1"""


Rectangle = __import__('9-rectangle').Rectangle
"""Write a class Square that inherits from Rectangle"""


class Square(Rectangle):
    """New class inhereted form rect"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
