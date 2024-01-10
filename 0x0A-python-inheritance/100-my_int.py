#!/usr/bin/python3
"""Defines a function that Write a class MyInt"""


class MyInt(int):
    """Write a class MyInt that inherits from int"""
    def __eq__(self, other):
        # Invert the behavior of ==
        return not super().__eq__(other)

    def __ne__(self, other):
        # Invert the behavior of !=
        return not super().__ne__(other)
