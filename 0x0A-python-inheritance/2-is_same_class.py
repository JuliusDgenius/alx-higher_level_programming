#!/usr/bin/python3
"""Module containing is_same_class function"""


def is_same_class(obj, a_class):
    """return True id object is exactly an instance of a class.
    Args:
        obj (object): class instance to check.
        a_class (class): The class to check obj with
    """
    if type(obj) is a_class:
        return True
    else:
        return False
