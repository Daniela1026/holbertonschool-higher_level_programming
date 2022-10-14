#!/usr/bin/python3
"""(list, dictionary, string, integer and boolean)"""


def class_to_json(obj):
    """
    Write a function that returns the dictionary description
    with simple data structure JSON
    """
    return obj.__dict__
