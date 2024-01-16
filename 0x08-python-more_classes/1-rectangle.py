#!/usr/bin/python3

"""Defines a rectangle"""


class Rectangle:
    """Represents a rectangle """

    def __init__(self, height=0, width=0):
        """It initialises width and height

        args:
            width - width of a rectanlge
            height - height of a rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """gets tyhe height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of a rectanlge"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """It gets the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
