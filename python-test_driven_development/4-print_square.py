#!/usr/bin/python3

'''function that prints a square with the character #'''


def print_square(size):
    '''print a square'''
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for z in range(size):
            print("#", end='')
        print()
