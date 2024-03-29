#!/usr/bin/python3
"""Define Square class"""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square object"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter to retrieve private attribute.
        Args:
            position (tuple): tuple of 2 positive integers
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets position
        Args:
            postion (tuple): tuple of 2 integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """computes the area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square the in stdout with the character #"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
