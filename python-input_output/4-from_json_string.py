#!/usr/bin/python3
"""(Python data structure) represented by a JSON string"""


import json


def from_json_string(my_str):
    """
    Returns an object JSON
    """
    return (json.loads(my_str))
