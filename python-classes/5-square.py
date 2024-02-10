#!/usr/bin/python3

'''defines a square'''


class Square:

    '''Super square'''

    def __init__(self, size=0) -> None:
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        assert isinstance(value, int), "size must be an integer"
        assert value >= 0, "size must be >= 0"
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size > 0:
            for i in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
        else:
            print("")
