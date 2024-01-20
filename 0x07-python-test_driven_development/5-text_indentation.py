#!/usr/bin/python3

"""Defines a function that prints a text"""


def text_indentation(text):
    """It represents a text"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_set = {'.', '?', ':'}

    line = ""
    for char in text:
        line += char
        if char in punctuation_set:
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip())
