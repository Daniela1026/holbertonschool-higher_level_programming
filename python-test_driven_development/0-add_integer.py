#!/usr/bin/python3
"""
import using __import__
"""
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")


def add_integer(a, b=98):
    """
    function that adds 2 integers
    Returns a + b
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    else:
        return a + b
