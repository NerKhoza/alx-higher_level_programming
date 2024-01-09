#!/usr/bin/python3

"""Defines a function that writes a string"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns 
    the number of characters written"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        num_characters_written = len(text)
        return num_characters_written
