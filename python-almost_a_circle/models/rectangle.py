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

    def update(self, *args, **kwargs):
        "Rectangle Update"
        for i, j in enumerate(args):
            if i == 0:
                self.id = j
            elif i == 1:
                self.width = j
            elif i == 2:
                self.height = j
            elif i == 3:
                self.x = j
            elif i == 4:
                self.y = j

        if args is None or len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """dictionary representation"""

        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['width'] = self.__width
        rect_dict['height'] = self.__height
        rect_dict['x'] = self.__x
        rect_dict['y'] = self.__y

        return rect_dict
