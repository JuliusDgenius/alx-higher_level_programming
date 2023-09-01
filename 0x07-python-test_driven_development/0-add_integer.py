#!/usr/bin/python3
"""
This module defines `add_integer function that computes
the sum of two integers
"""

def add_integer(a, b=98):
    """Adds two integers
    Args:
        a (int): The first integer to add.
        b (int): The second integer to add. Takes value 98 if no
        value is provided.
        Return: Returns the sum of the addition of a and b
    Raises:
        int: sum of a and b
    """
    if isinstance(a, str) or a is None:
        raise TypeError("a must be an integer")
    if isinstance(b, str):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
