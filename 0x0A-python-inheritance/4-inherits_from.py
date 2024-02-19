#!/usr/bin/python3
"""object is an instance of a class it inherited"""


def inherits_from(obj, a_class):
    """checks the object"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        """Function that checks"""
        return True
    return False
