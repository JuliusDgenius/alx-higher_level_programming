#!/usr/bin/python3
"""Module defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines the Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes class instance
        Args:
            width (int): width
            height (int): height
            x (int): x-coordinate
            y (int): y-coordinate
            id (int): ID of class instance
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value
        Args:
            value (int): width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height
        Args:
            value (int): height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets x-coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x-coordinate
        Args:
            value (int): x value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets y-coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y-coordinate
        Args:
            value (int): y value
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes the area of the rectangle"""
        return self.__height * self.__width
