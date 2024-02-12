#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Empty Class"""
    def __init__(self, width=0, height=0):
        """ instance attributes
        Args:
               width (int): shortest side of rectangle
               height (int): longest side of rectangle
        """
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """Getting the width  of the rectangle"""
        return self.__width
    @width.setter
    def width(self, value):
        """setting the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
