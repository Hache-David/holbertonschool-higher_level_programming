#!/usr/bin/python3
''' function that returns the list of available
attributes and methods of an object'''


def lookup(obj):
    '''copy obj in new list'''
    return dir(obj)
