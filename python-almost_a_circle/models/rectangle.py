#!/usr/bin/python3
"Class Rectangle"


from models.base import Base


class Rectangle(Base):
    "Class Rectangle"

    def __init__(self, width, height, x=0, y=0, id=None):
        "Class constructor"
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        "Rectangle private instance attributes, width getter"
        return (self.__width)

    @width.setter
    def width(self, value):
        "Rectangle private instance attributes, width setter"
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        "Rectangle private instance attributes, height getter"
        return (self.__height)

    @height.setter
    def height(self, value):
        "Rectangle private instance attributes , width setter"
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        "Rectangle, x getter"
        return (self.__x)

    @x.setter
    def x(self, value):
        "Rectangle, x setter"
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        "Rectangle, y getter"
        return (self.__y)

    @y.setter
    def y(self, value):
        "Rectangle, y setter"
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
