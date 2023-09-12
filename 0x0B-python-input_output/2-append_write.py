#!/usr/bin/python3
"""Defines a funtion that appends text to a file"""


def append_write(filename='', text=''):
    """Appends a string to the end of a UTF* text file
    Args:
        filename (str): Tne file name to append to.
        text (str): The string to append to file
    Returns:
        The number of characters appended.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return (f.write(text))
