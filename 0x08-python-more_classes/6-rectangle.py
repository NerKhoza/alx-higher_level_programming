#!/usr/bin/python3

"""Defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        result = ""
        for i in range(self.height):
            result += "#" * self.width + "\n"
        return result.rstrip()

    def __repr__(self):
        """Returns a string representation of the rectangle for recreation"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a farewell message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
