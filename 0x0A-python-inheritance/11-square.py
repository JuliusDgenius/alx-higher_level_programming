#!/usr/bin/python3
"""
This module implements a Square object
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initiatization
        Args:
            size (int): size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
