#!/usr/bin/python3
"""Module containing inherits_from method."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a_class; else False.
    Args:
        obj (object): The object to compare.
        a_class (class): Class to compare obj with.
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
