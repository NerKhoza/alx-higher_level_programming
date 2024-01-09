#!/usr/bin/python3

"""Defines a function that appends a string"""


def append_write(filename="", text=""):
    """ a function that appends a string"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
