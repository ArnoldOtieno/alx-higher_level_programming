#!/usr/bin/python3
"""checks if an object is exactly an instance of a specified class """


def is_same_class(obj, a_class):
    """obj is the instance being checked"""
    if type(obj) == a_class:
        """function that checks"""
        return True
    else:
        return False
