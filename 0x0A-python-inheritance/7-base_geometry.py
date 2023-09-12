#!/usr/bin/python3
"""Module containing base_geometry base class."""


class BaseGeometry:
    """Defines geometry Base class"""
    def __init__(self):
        """initialize instance"""
        pass

    def area(self):
        """Area method that does nothing but raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Args:
            name (str): string name
            value (value): value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
