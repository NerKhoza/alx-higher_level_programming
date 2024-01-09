#!/usr/bin/python3
"""Defines a function that creates an object"""
import json


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    :param filename: The name of the JSON file.
    :return: The loaded object.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
