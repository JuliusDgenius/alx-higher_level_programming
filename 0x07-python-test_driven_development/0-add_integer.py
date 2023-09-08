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
    values = []
    for x, parameter in [(a, "a"), (b, "b")]:
        if isinstance(x, int):
            values.append(x)
        elif isinstance(x, float):
            values.append(int(x))
        else:
            raise TypeError("{} must be an integer".format(parameter))
    return sum(values)
