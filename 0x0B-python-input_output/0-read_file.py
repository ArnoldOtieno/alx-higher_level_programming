#!/usr/bin/python3
def read_file(filename=""):
    """reading a text file"""
    with open(filename, encoding='utf-8') as mfile:
        print(mfile.read(), end="")
