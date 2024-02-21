#!/usr/bin/python3
'''Write a class Rectangle that inherits from
BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Represent a rectangle using BaseGeometry.'''

    def __init__(self, width, height) -> None:
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        str_return = f"[Rectangle] "
        str_return += f"{self.__width}/{self.__height}"
        return str_return

    def area(self):
        return self.__height * self.__width
