#!/usr/bin/python3
"""Defines a function that returns the dictionary"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    if not hasattr(obj, '__dict__'):
        raise ValueError("Object is not serializable")

    serialized_data = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_data[key] = value
        elif hasattr(value, '__dict__'):
            serialized_data[key] = class_to_json(value)

    return serialized_data
