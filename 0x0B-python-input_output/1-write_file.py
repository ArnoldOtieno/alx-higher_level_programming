#!/usr/bin/python3
"""this function writes to a file"""


def write_file(filename="", text=""):
    """function that writes to the file"""
    with open(filename, mode='w', encoding='utf-8') as mfile:
        return mfile.write(text)
