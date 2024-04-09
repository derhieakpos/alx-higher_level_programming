#!/usr/bin/python3
"""
This model represents a square
"""


class Square:

    """
    this class represents a square

    Attributes:
        __size (int): sixe of a square

    Methods:
        there are no methods in this class
    """
    def __init__(self, size=0):
        """
        Initialization of a class instance

        Args:
            size: the size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
