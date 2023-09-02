#!/usr/bin/python3
"""
This is '4-print_square' module
The module supplies the function, 'print_square(size)' 
which prints a square of a given size with the character
"""


def print_square(size):
    """This function prints a square with the character '#'
    Args:
        size (int): The size of the square to be printed.
        Return: printed square.
    """
    if type(size) is float or type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = 0
    while i < size:
        print(size * '#')
        i += 1
