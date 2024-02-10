#!/usr/bin/python3

'''defines a square'''


class Square:

    '''Super square'''

    def __init__(self, size=0, position=(0, 0)) -> None:
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        assert isinstance(value, int), "size must be an integer"
        assert value >= 0, "size must be >= 0"
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        assert isinstance(
            value, tuple), "position must be a tuple of 2 positive integers"
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size > 0:
            for x in range(0, self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print()
        else:
            print("")
