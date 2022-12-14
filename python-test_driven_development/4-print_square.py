#!/usr/bin/python3
""" Module print square """


def print_square(size):
    """ print a column and row of '#' """
    if type(size) is not int or type(size) is float:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print("#" * size)
