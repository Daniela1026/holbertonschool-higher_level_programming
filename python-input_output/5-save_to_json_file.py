#!/usr/bin/python3
"""Object to a text file, using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """write function that writes an Object JSON"""
    with open(filename, 'w+') as txt:
        json.dump(my_obj, txt)
