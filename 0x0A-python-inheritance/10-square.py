#!/usr/bin/python3
"""Module containing class Square that inherits from REctangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines Square class that inherits from Rectangle parent"""
    def __init__(self, size):
        """Instantiates a Square instance
        Args:
            size (int): Size of the square instance
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
