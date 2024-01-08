#!/usr/bin/python3
"""Defines a class checking function."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a given class
    Args:
        obj:The object to check.
        a_class:Th class to match he type of obj to.
    Return:
        if obj is exactly an instance of a_class - True.
        Otherwise - False"""
    if type(obj) == a_class:
        return True
    return False
