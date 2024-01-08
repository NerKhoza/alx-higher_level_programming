#!/usr/bin/python3
"""Defines a class checking function."""
def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    :param obj: The object to check.
    :param a_class: The specified class to check for inheritance.
    :return: True if obj is an instance of a subclass, False otherwise.
    """

    if issubclass (type(obj), a_class) and type(obj) != a_class:
        return True
    return False
