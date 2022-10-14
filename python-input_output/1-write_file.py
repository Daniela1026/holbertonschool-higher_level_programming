#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """returns the number of characters written"""
    with open(filename, 'w') as txt:
        number = txt.write(text)
        return number
