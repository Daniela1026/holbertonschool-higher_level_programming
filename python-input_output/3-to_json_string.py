#!/usr/bin/python3
"""Write a function that returns the JSON"""


import json


def to_json_string(my_obj):
    """representation of an object (string)"""
    toJSON = json.dumps(my_obj)
    return toJSON
