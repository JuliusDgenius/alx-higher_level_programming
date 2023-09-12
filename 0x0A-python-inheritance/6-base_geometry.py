#!/usr/bin/python3
"""Module containing base_geometry base class."""


class BaseGeometry:
    """Defines geometry Base class"""
    def area(self):
        """Area method that does nothing but raise an exception"""
        raise Exception("area() is not implemented")
