#!/usr/bin/python3
"""Module defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines the Rectangle class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class instance
        Args:
            width (int): width of the rectangle instance.
            height (int): height of the rectangle instance.
            x (int): x plane
            y (int): y plane
            id (int): object id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def get_width(self):
        """width getter"""
        return self.__width

    @property
    def get_height(self):
        """height getter"""
        return self.__height

    @property
    def get_x(self):
        """x getter"""
        return self.__x

    @property
    def get_y(self):
        """x getter"""
        return self.__y

    @width.setter
    def set_width(self, value):
        """sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def set_height(self, value):
        """height setter"""
        if type(value) is not int:
            TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @x.setter
    def set_x(self, value):
        """Sets x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def set_y(self, value):
        """Sets x"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__x = value
