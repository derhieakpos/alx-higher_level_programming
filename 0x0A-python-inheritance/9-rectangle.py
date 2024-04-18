#!/usr/bin/python3
"""
A module that holds the rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class for a rectangle
    """

    def __init__(self, width, height):
        """
        Initialise the class

        Args:
            width: the width
            height: the height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

        def area(self):
            """
            a method that returns the area
            """
            return self.__width * self.__height

        def __str__(self):
            """
            str special method
            """
            return "[Rectangle] {}/{}".format(self.__width, self.__height)
