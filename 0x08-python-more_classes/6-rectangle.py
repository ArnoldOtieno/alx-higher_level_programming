#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Empty Class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ instance attributes
        Args:
               width (int): shortest side of rectangle
               height (int): longest side of rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting/setting the width  of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting/setting the height  of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculating area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculating perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        """printing rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        store = []
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                store.append('#')
            if i != self.__height - 1:
                store.append("\n")
        return ("".join(store))

    def __repr__(self):
        """repr function """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """delete an instance"""
        type(self).number_of_instances -= 1
        print(f"Bye rectangle...")
