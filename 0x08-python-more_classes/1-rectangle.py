#!/usr/bin/python3

"""Defines a class Rectangle"""


class Rectangle:
    """It represents a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    """gets the width of a rectangle"""
    def width(self):
        return self.__width

    @width.setter
    """sets the width of a rectangle"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of a rectangle"""
        return self.__height

    @height.setter
    """sets the height of a rectangle"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
