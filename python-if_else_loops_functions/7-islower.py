#!/usr/bin/env python3
# 7-islower.py

def islower(c):
    if ord(c) in range(65, 91):
        return False
    elif ord(c) in range(97, 123):
        return True
    else:
        return False
