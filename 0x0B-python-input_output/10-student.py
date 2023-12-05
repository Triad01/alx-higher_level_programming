#!/usr/bin/python3
"""Module contains a student class"""


class Student:
    """This defines the student class with some attributes"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs is None or not isinstance(attrs, list):

            return self.__dict__
        else:
            return {attr: getattr(self, attr, None) for attr in attrs}
