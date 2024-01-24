#!/usr/bin/python3

def pow(a, b):
    index = a
    if b == 0:
        a = 1
    if b < 0:
        while b != 1:
            a = a / index
            b += 1
    else:
        while b != 1:
            a = a * index
            b -= 1
    return a
