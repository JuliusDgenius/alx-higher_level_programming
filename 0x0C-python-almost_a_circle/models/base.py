#!/usr/bin/python3
"""Module that defines the class Base"""
import json
import csv
import turtle


class Base:
    """Defines the Base class which is the parent class."""
    __nb_objects = 0    # private class attribute

    def __init__(self, id=None):
        """Instance Constructor
        Args:
            id (int): ID of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that return the JSON string representation of
            list_dictionaries
        Args:
            list_dictionaries (list): A list of dictionary
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A class method that writes the JSON string represemtation
        of list_obj to a file
        Args:
            list_objs (list): A list of a class instance objects
        """
        filename = cls.__name__ + ".json"
        empty_list = []
        with open(filename, "w") as json_file:
            if list_objs is None:
                return json_file.write("[]")
            else:
                for list_obj in list_objs:
                    empty_list = [list_obj.to_dictionary() for list_obj
                                  in list_objs]
                json_file.write(Base.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string (str): is a string representing a list of dictionaries
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes set already.
        Args:
            dictionary (dict): A double pointer to a dictionary
        """
        if cls.__name__ == 'Rectangle':
            new_rect = cls(1, 1)
        else:
            new_rect = cls(1)

        if dictionary:
            new_rect.update(**dictionary)
        return new_rect

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
            return [cls.create(**d) for d in list_dicts]
        except IOError:
            if i == 0:
                self.id = a
            elif i == 1:
                self.size = a
            elif i == 2:
                self.x = a
            elif i == 3:
                return []

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as json_file:
                list_dicts = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV encoding of a list object to a file.
        Args:
            list_objs (list): A list of inherited Base instance
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    key_names = ["id", "width", "height", "x", "y"]
                else:
                    key_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=key_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes initialized from CSV file.
        """
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r', newline='') as csv_file:
                if cls.__name__ == "Rectangle":
                    key_names = ["id", "width", "height", "x", "y"]
                else:
                    key_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_file, fieldnames=key_names)
                list_dicts = [dict([k, int(v)] for k, v in
                              d.items()) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def draw(list_rectangles, list_squares):
        """Draws a rectangle and square in a new window
        Args:
            list_rectangles (list): list of rectangles
            list_squares (list): list of squares
        """
        screen_width = 620
        padding = 10
        row_width = padding
        row_height = 0
        screen_height = padding
        color_list = ["red", "orange", "yellow", "green", "blue",
                      "indigo", "violet"]
        color_size = len(color_list)
        color_index = 0

        for rect in list_rectangles:
            potential_width = row_width + rect.width < screen_width
            + rect.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += square.size + square.x + padding
                if (row_height < square.size + square.y):
                    row_height = square.size + square.y
            else:
                screen_height += row_height + padding
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y
        turtle.screensize(canvwidth=screen_width, canvheight=screen_height)
        turtle.pu()
        turtle.left(180)
        turtle.forward(screen_width/2 - padding)
        turtle.right(9)
        row_width = padding
        row_height = 0

        for rect in list_rectangles:
            potential_width = row_width + rect.width + rect.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += rect.height + rect.x + padding
                if (row_height < rect.height + rect.y):
                    row_height = rect.height + rect.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = rect.width + rect.x + padding * 2
                row_height = rect.height + rect.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(rect.x)
            turtle.right(90)
            turtle.forward(rect.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(rect.width + padding)
            turtle.left(90)
            turtle.forward(rect.y)
            turtle.right(90)

        for square in list_squares:
            potential_width = row_width + square.size + square.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += square.size + square.x + padding
                if (row_height < square.size):
                    row_height = square.size + square.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(square.x)
            turtle.right(90)
            turtle.forward(square.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(square.size + padding)
            turtle.left(90)
            turtle.forward(square.y)
            turtle.right(90)

        turtle.getscreen()._root.mainloop()
