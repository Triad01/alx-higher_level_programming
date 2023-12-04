#!/usr/bin/python3
def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    ; otherwise False"""
    if issubclass(object, a_class) or type(obj) is not a_class:
        return True
    else:
        return False
