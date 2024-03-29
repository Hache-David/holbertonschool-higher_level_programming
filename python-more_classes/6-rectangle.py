#!/usr/bin/python3

'''class Rectangle that defines a rectangle'''


class Rectangle:
    '''Super rectangle'''
    number_of_instances = 0

    def __init__(self, width=0, height=0) -> None:
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.height

    def perimeter(self):
        if self.__height != 0 and self.__width != 0:
            return ((2 * self.__height) + (2 * self.__width))
        else:
            return 0

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        str_return = ""
        for i in range(self.__height):
            str_return += "#" * self.__width + '\n'
        return str_return.strip("\n")

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
