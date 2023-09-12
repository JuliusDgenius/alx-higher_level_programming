#!/usr/bin/python3
"""MyList class module"""


class MyList(list):
    """Class MyList that inherits from list
    Args:
        list (class): super class MyList will inherit from.
    """
    # public instance method
    def print_sorted(self):
        """prints a sorted list."""
        print(sorted(self))
