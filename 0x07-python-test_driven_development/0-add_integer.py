#!/usr/bin/python3

"""
This module adds two numbers that are integers and float type
"""

def add_integer(a, b=98):
    """
    This function adds two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        The sum of two numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + (b)
