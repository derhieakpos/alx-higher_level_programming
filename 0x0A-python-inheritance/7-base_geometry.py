#!/usr/bin/python3
"""
A module that executes  geometric functions
"""



class BaseGeometry:
    """
    An empty class
    """

    def area(self):
        """
        this method raises a exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        this method validates the value

        Args:
            name: the name
            value: the value

        Raises:
            TypeError: if value is not int
            ValueError: id value is less than or equal to zero
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
