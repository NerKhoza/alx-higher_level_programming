#!/usr/bin/python3

"""Defines a function that returns the JSON"""

import json


def to_json_string(my_obj):
    """
    Convert the given Python object to its JSON representation.

    Parameters:
    - my_obj: The Python object to be converted.

    Returns:
    A JSON-formatted string representing the input object.
    """
    return json.dumps(my_obj)
