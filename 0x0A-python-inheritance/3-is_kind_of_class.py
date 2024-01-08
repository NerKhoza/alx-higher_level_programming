#!/usr/bin/python3
"""Defines a class checking function."""

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.

    :param obj: The object to check.
    :param a_class: The specified class to check against.
    :return: True if obj is an instance of a_class or a subclass of
        a_class, False otherwise."""

    if isinstance (obj, a_class):
        return True
    return False
