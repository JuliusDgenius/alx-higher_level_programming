#!/usr/bin/python3
"""Module that defines the class Base"""


class Base:
    """Defines the Base class which is the parent class."""
    __nb_objects = 0 # private class attribute
    def __init__(self, id=None):
        """Instance Constructor
        Args:
            id (int): ID of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
