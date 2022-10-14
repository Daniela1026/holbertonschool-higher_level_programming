#!/usr/bin/python3
"""Write a function that creates an Object"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”
    """
    with open(filename, "r", encoding="utf-8") as i:
        return(json.load(i))
