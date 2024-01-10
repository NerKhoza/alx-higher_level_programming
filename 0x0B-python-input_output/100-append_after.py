#!/usr/bin/python3
"""Defines a  function that inserts a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """ Open the file in read mode"""
    with open(filename, 'r') as file:
        """ Read all lines from the file"""
        lines = file.readlines()

    """ Open the file in write mode to overwrite its contents"""
    with open(filename, 'w') as file:
        """ Iterate through each line"""
        for line in lines:
            """ Write the current line to the file"""
            file.write(line)

            """ Check if the search string is present in the current line"""
            if search_string in line:
                """ If found, append the new string after the current line"""
                file.write(new_string + '\n')
