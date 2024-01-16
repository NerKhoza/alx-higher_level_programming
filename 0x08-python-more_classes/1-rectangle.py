#!/usr/bin/python3

"""Defines a class Rectangle"""


class Rectangle:
    """It represents a rectangle"""

    def __init__(self, height=0, width=0):
        """It initialises height and width

        args:
            height - height of the rectangle
            width - width of rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """gets the height of a rectangle"""
        return self.__height

    @property
    def width(self):
        """gets the width of a rectangle"""
        return self.__width

    @height.setter
    def height(self, value):
        """sets the height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """sets the width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
