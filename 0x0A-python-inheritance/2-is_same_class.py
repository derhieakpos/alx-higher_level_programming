#!/usr/bin/python3
"""
A module that return True if the obj is an exact instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    The function detects if obj is True or False
    Obj:
        the object to be detected
    a_class:
        the type of object
    Returns:
        if the object is True or False
    """

    return type(obj) is a_class
