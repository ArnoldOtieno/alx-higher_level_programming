#!/usr/bin/python3
"""This function prints list in sorted order"""


class MyList(list):
    """mylist inherits properties from list"""
    def print_sorted(self):
        """print in sorted ascending manner"""
        print(sorted(self))
