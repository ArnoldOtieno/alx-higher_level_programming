#!/usr/bin/python3

"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """inherits from  checks the inheritance of obj"""
    if issubclass(type(obj), a_class) and (type(obj) != a_class):
        """issubclass verifies the obj"""
        return True
    return False
