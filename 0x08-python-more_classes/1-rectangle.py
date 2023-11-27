#!/usr/bin/python3
""" This module defines the rectangle class
    This class represents a rectangle with some attributes and methods
"""


class Rectangle:
    """
    This is a brief description of the class
    Attributes:
        width: width of the rectangle
        height: height of the rectangle
    """
    def __init__(self, width=0, height=0):

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """sets the width of the object"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the object"""
        if not isinstance(value, int):

            raise TypeError("width must be an integer")

        if value < 0:

            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """gets the height of the object"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of the object"""
        if not isinstance(value, int):

            raise TypeError("height must be an integer")

        if value < 0:

            raise ValueError("height must be >= 0")

        self.__height = value
