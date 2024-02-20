#!/usr/bin/python3
"""text fie reading function"""


def read_file(filename=""):
    """reading a text file"""
    with open(filename, encoding='utf-8') as mfile:
        print(mfile.read(), end="")
