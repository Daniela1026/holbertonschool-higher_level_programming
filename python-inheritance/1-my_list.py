#!/usr/bin/python3
"""module my list"""


class MyList(list):
    """
    that prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        print(sorted(self))
