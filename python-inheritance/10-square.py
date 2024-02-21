#!/usr/bin/python3
'''Write a class Square that inherits from Rectangle (9-rectangle.py):'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square'''
    def __init__(self, size) -> None:
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''AREA'''
        return self.__size ** 2
