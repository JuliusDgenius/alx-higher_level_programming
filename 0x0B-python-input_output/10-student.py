#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): The first name of student
            last_name (str): The last name of student
            age (int): Age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attruibutes
        included in the list,
        Args:
            attrs (list): (Optional) the attributes to represent.
        """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
