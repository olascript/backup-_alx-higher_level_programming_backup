#!/usr/bin/python3
"""
Defines a Rectangle Class
"""


class Rectangle:
    """Represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Defines  a Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """setter of private instance width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of private instance width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """setter of private instance height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of private instance height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of a square"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeters of a square"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a square"""
        string = ""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """Represents a rectangle"""
        return "Rectangle(" + str(self.__width) + ", " \
                            + str(self.__height) + ")"

    def __del__(self):
        """deletion of instance"""
        print("Bye rectangle...")

