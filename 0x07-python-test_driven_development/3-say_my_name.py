#!/usr/bin/python3
"""Defines a function that prints a string"""

def say_my_name(first_name, last_name=""):
    """Represents a function that prints a string
    args:
        first_name - parameter 1
        last_name - parameter 2
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string and last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
