#!/usr/bin/python3
"""this function returns list of available methods and attributes"""

def lookup(obj):
    """store is the variable that stores the variables and methods of obj"""

    return (list(dir(obj)))
