#!/usr/bin/python3
"""Base Class Python"""

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

            @staticmethod
            def to_json_string(list_dictionaries):
                """JSON is one of the standard formats"""
                if list_dictionaries is None or len(list_dictionaries) == 0:
                    return "[]"

                return json.dumps(list_dictionaries)
