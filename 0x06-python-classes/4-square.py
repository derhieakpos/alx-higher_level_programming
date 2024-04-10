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
        the multiplication of the size
    """
    def __init__(self, size=0):
        """
        Initialization of a class instance

        Args:
            size: the size of the square
        """
        self.__size = 0
        self.size = size

    def area(self):
        """
        this calculates the arera of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        method that return the private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        method that sets the size

        Args:
            value (int): value to be set
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
