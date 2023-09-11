#!/usr/bin/python3

"""The module contains a function that displays list of attributes.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an obj.
    Args:
        obj (list): The object which list to return.
    """
    list_of_attr = dir(obj)
    return list_of_attr
