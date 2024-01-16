#!/usr/bin/python3
"""Defines a class rectangle"""


class Rectangle:
    """represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialises new rectangle

        args:
            width - width of a rectangle
            height - height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width of a rectanle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of a rectanle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets height of a rectanle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of a rectanle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of a rectanle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of a rectanle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Represents the printable representation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = ""
            for _ in range(self.__height):
                result += '#' * self.__width + '\n'
            return result.rstrip()
