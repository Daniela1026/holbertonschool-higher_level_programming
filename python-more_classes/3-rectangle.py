#!/usr/bin/python3
""" module string representation"""


class Rectangle:
        """class Rectangle representation"""

        def __init__(self, width=0, height=0):
                """Initializer object with width and height values."""

                self.width = width
                self.height = height

        @property
        def width(self):
                """Convert the atribute width to a atribute
                editable with self.width
                """
                return self.__width

        @width.setter
        def width(self, value):
                """Assined te value to width with the variable value"""

                if not isinstance(value, int):
                        raise TypeError("width must be an integer")
                if value < 0:
                        raise ValueError("width must be >= 0")
                self.__width = value

        @property
        def height(self):
                """Convert the atribute height to the attribute
                editable with self.height
                """

                return self.__height

        @height.setter
        def height(self, value):
                """Assinded the value to self"""

                if not isinstance(value, int):
                        raise TypeError("height must be an integer")
                if value < 0:
                        raise ValueError("height must be >= 0")
                self.__height = value

        def area(self):
                """Return the area of the rectangle"""

                return (self.__width * self.__height)

        def perimeter(self):
                """return perimeter of the rectangle"""

                if self.__width == 0 or self.__height == 0:
                        return 0
                return ((self.__width * 2) + (self.__height * 2))

        def __str__(self):
            """Return the printable representation of the Rectangle.
            Represents the rectangle with the # character.
            """

            string_rectagle = ""
            if self.__width <= 0 or self.__height <= 0:
                return string_rectagle

            for i in range(self.__height):
                string_rectagle += ('#' * self.__width)
                if i < (self.__height - 1):
                    string_rectagle += '\n'
            return string_rectagle
