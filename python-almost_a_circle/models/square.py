#!/usr/bin/python3

"""Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The overloading __str__ method should return"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Returns the size of the object"""
        return self.width

    @size.setter
    def size(self, value):
        """Returns the size of the object"""
        self.width = value
        self.height = value
