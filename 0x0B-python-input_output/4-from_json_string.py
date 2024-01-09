#!/usr/bin/python3
"""Defines a function that returns an object"""

import json


def from_json_string(my_str):
    """Convert a JSON string to a Python data structure.

    Args:
        my_str(str): JSON string to be converted

    Return:
         returns an object represented by a JSON string
        """
    obj = json.loads(my_str)
    return obj
