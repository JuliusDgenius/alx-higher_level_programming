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

    def display(self):
        """Method to print Rectangle to stdout"""
        if (self.width == 0) or (self.height == 0):
            print()
            return

        [print() for y in range(0, self.y)]
        for h in range(0, self.height):
            [print(" ", end="") for x in range(0, self.x)]
            [print("#", end="") for w in range(0, self.width)]
            print()

    def __str__(self):
        """Returns a string representation of a Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
