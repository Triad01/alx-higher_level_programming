#!/usr/bin/python3
def read_file(filename=""):
    """reads file and prints it to stdout"""
    with open(filename, "r") as my_file:
        data = my_file.read()
        print(data)
