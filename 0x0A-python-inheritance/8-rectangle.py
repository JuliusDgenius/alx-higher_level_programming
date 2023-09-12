#!/usr/bin/python3
"""Module the defines Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines Rectangle class to inherit from BaseGeometry class"""
    def __init__(self, width, height):
        """Initializes class instance
        Args:
            width (int): The rectangle width
            height (int): The rectangle height
        """
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        def area(self):
            """Area of Rectangle instance"""
            raise Exception("area() is not implemented")
