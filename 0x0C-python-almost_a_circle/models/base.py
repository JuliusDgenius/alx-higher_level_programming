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

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that return the JSON string representation of
            list_dictionaries
        Args:
            list_dictionaries (list): A list of dictionary
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A class method that writes the JSON string represemtation
        of list_obj to a file
        Args:
            list_objs (list): A list of a class instance objects
        """
        filename = cls.__name__ + ".json"
        empty_list = []
        with open(filename, "w") as json_file:
            if list_objs is None:
                return json_file.write("[]")
            else:
                for list_obj in list_objs:
                    empty_list = [list_obj.to_dictionary() for list_obj
                                  in list_objs]
                json_file.write(Base.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string (str): is a string representing a list of dictionaries
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes set already.
        Args:
            dictionary (dict): A double pointer to a dictionary
        """
        if (dictionary):
            if cls.__name__ == 'Rectangle':
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
            return [cls.create(**d) for d in list_dicts]
        except IOError:
            if i == 0:
                self.id = a
            elif i == 1:
                self.size = a
            elif i == 2:
                self.x = a
            elif i == 3:
                return []

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as json_file:
                list_dicts = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
