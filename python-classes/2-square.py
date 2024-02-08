#!/usr/bin/python3
'''defines a square'''


class Square:
    '''Super square'''

    def __init__(self, size=0) -> None:
        assert isinstance(size, int), "size must be an integer"
        assert size >= 0, "size must be >= 0"
        self.__size = size
