#!/usr/bin/python3
"""Module that defines the class Base"""
import json


class Base:
    """Defines the Base class which is the parent class."""
    __nb_objects = 0    # private class attribute

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

    def to_json_string(list_dictionaries):
        """static method that return the JSON string representation of
            list_dictionaries
        Args:
            list_dictionaries (list): A list of dictionary
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
