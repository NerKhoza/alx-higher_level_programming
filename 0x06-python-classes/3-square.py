#!/usr/bin/python3

"""Defines a square"""


class Square:
    """Represents a sqaure"""

    def __init__(self, size=0):
        """Initiatlises size"""
        if not isinstance(size, int):
            raise("size must be an integer")
        elif size < 0:
            raise("size must be >= 0")
        self.__size = size

    def area(self):
        """Initialises area"""
        return (self.__size * self.__size)
