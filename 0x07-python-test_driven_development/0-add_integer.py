#!/usr/bin/python3

""" Defines a function that adds two integers"""


def add_integer(a, b=98):
    """
    Represents a function that that adds two integers

    args:
        a - first intger
        b - second integer
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer ")

    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer ")

    a = int(a)
    b = int(b)

    return a + b
