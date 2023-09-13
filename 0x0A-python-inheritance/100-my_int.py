#!/usr/bin/python3
"""Module containing MyInt class that inherit from int"""


class MyInt(int):
    """Defines class that inherits from int parent class"""
    
    def __eq__(self, val):
        """Inverts the behaviour of == with !="""
        return self.real != val

    def __ne__(self, val):
        """Inverts != behaviour with that of =="""
        return self.real == val
