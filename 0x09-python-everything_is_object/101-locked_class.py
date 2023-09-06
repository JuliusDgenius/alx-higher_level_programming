#!/usr/bin/python3
"""This module defines a locked class, LockedClass"""


class LockedClass:
    """A locked class that prevents the user from dynamaically
    creating new instance attribute, except first_name
    """

    __slots__ = ["first_name"]
