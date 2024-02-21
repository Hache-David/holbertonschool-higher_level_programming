#!/usr/bin/python3
'''Write a class Square that
inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).'''
Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    def __init__(self, size) -> None:
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        str_return = f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
        return str_return
