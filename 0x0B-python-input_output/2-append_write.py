#!/usr/bin/python3
"""this function appends to a file"""


def append_write(filename="", text=""):
    """funtion that appends text"""
    with open(filename, mode='a', encoding='utf-8') as mfile:
        return mfile.write(text)
