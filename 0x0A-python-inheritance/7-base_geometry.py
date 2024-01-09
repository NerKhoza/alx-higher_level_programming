#!/usr/bin/python3
"""Defines a geometry class BaseGeometry"""

class BaseGeometry:
    """Represents a base geometry"""

    def area(self):
        """Not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an intege
        Args:
            name(str): name of the parameter
            value:the parameter to alidate
        Raises:
            TypeError: if value is not an integer
            ValeuError: if value <= 0.
            """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
