#!/usr/bin/python3
"""
This is the '5-text_indentation' module.
Contains 'text_indentation(text)' funtion.
"""


def text_indentation(text):
    """Function that prints a text with 2 new line after .,? and :
    Args:
        text (str): The string to print with indentation
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        if c == " ":
            continue
        print(c, end="")
        if (c == '.' or c == '?' or c == ':'):
            print("")
            print("")
