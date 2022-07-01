#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevents the user from creating new instance of lockedClass attributes
    except the attribute is 'first_name'
    """

    __slots__ = ["first_name"]
