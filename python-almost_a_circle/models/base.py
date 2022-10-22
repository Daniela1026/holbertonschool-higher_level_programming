#!/usr/bin/python3
"""Base Class """
import json


class Base:
    """ Write the first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id

        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

