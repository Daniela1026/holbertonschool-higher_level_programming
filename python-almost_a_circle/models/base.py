#!/usr/bin/python3
"""Base Class """


class Base:
    """ Write the first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON is one of the standard formats for sharing data
        representation"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
        return json.dumps(list_dictionaries)
