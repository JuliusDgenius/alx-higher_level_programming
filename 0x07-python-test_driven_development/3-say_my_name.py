#!/usr/bin/python3
"""
This is the '3-say_my_name' module.
This module supplies the function, 'say_my_name' that prints the \
        first name and lastname
"""


def say_my_name(first_name, last_name=""):
    """This function prints the firstname and lastname given as arguments
    Args:
        first_name (str): A string representing first name
        last_name (str): represents the last name.
        Return: prints name supplied as arguments.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
