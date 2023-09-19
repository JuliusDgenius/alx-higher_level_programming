#!/usr/bin/python3
"""Module that defines the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherit from Rectangleclass"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square instance
        Args:
            size (int): size of the square instance
            x (int): x-coordinate of the square
            y (int): y-coordinate of the square
            id (int): ID of the square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """Gets size"""
        return self.width

    @size.getter
    def size(self, value):
        """Sets size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
                if "size" in kwargs:
                    self.width = kwargs["size"]
                    if "x" in kwargs:
                        self.x = kwargs["x"]
                        if "y" in kwargs:
                            self.y = kwargs["y"]

    def to_dictionary(self):
        """Return the dictionary representation of the Square"""
        return ({"id": self.id, "size": self.width, "x": self.x, "y": self.y})
