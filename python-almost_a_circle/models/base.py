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

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON is one of the standard formats"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as i:
            jsson = []
            if list_objs is not None:
                for a in list_objs:
                    jsson.append(cls.to_dictionary(a))
                i.write(cls.to_json_string(jsson))
            else:
                i.write(cls.to_json_string(jsson))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
       """that returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

     @classmethod
    def load_from_file(cls):
        """that returns a list of instances"""
        name = cls.__name__ + '.json'
        emptylist = []
        listt = []
        try:
            with open(name, mode='r', encoding='UTF8') as files:
                aux = files.read()
                emptylist = cls.from_json_string(aux)
                """List of dicts"""
                for elem in emptylist:
                    auxone = cls.create(**elem)
                    listt.append(auxone:x)
                return listt
        except FileNotFoundError:
            return emptylist
