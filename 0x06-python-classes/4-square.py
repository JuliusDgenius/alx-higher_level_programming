#!/usr/bin/python3
"""Define Square class"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initializes a square object"""
        self.size = size
    
    @property
    def size(self):
        """Gets private attribute
        Args:
            size (int): size of the the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets value
        Args: 
            value (int): the value to set
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """computes the area of a square"""
        return (self.__size * self.__size)
