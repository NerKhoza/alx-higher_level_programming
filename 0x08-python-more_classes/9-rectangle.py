#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """ Public class attributes

        number_of_instances - number of rectangle instances
        print_symbol - symbol used for strng represebtation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Private instance attributes

        args:
            width - width of a rectanle
            height - height of a rectanlge
        """
        self.__width = 0
        self.__height = 0

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets a width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets a width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets a height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of a rectangle"""
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
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        """ Decrement number_of_instances"""
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2i

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance"""
        return cls(size, size)
