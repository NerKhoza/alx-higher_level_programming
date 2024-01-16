#!/usr/bin/python3
"""Defines a class rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialises width and height

            args:
                width - width of a rectangle
                height - of a rectanlge
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the widt of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        return 2 * (self.width + self.height)
