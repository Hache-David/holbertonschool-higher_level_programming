#!/usr/bin/env python3

'''def islower(c):
    if ord(c) in range(65, 91):
        return False
    elif ord(c) in range(97, 123):
        return True
    else:
        return False
'''
def islower(c):

    if ord(c) >= 97 and ord(c) <= 122:
        return False
    else:
        return True
