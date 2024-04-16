#!/usr/bin/python3
"""
A module that returns a boolean:
    True if object matches the instance
    False otherwise
"""


def inherits_from(obj, a_class):
    """
    A function that checks the object's instance
        
    Args:
        obj: the object
        a_class: the instance

    Returns: True if objects matches instance, false otherwise
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
