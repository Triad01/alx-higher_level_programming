#!/usr/bin/pythond
"""appends to file"""


def append_write(filename="", text=""):
    """appends to a file if exists or create"""

    with open(filename, "a") as file:

        char = file.write(text)

        return char
