#!/usr/bin/python3
""" module contains the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherist from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns printable string representatin"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """getter function for the size"""
        return f"{self.width}"

    @size.setter
    def size(self, value):
        """setter for the size"""

        if not isinstance(value, int):

            raise TypeError("width must be an integer")

        if value <= 0:

            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update function"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        elif kwargs:

            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representatin of object"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y
        }
