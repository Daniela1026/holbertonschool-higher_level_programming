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

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #,x,y"""
        for i in range(self.y):
            print()

        for h in range(self.__height):
            for n in range(self.x):
                print(' ', end='')
            for w in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """the __str__ method so that it returns"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **keyargs):
        """ Update rectangle by adding the public method"""

        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.__width = args[1]
                if i == 2:
                    self.__height = args[2]
                if i == 3:
                    self.__x = args[3]
                if i == 4:
                    self.__y = args[4]
        else:
            if 'id' in keyargs:
                self.id = keyargs['id']
            if 'width' in keyargs:
                self.__width = keyargs['width']
            if 'height' in keyargs:
                self.__height = keyargs['height']
            if 'x' in keyargs:
                self.__x = keyargs['x']
            if 'y' in keyargs:
                elf.__y = keyargs['y']
