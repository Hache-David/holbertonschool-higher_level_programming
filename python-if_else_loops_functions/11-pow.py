#!/usr/bin/python3

def pow(a, b):
    index = a
    if a == 0:
        return a
    if b == 0:
        a = 1
        return a
    if b < 0:
        while b != 1:
            a = a / index
            b += 1
    if b > 1:
        while b != 1:
            a = a * index
            b -= 1
    return a