#!/usr/bin/python3
"""if object is an instance of"""


def is_kind_of_class(obj, a_class):
    """cheking the instance"""
    if isinstance(obj, a_class):
        return True
    return False
