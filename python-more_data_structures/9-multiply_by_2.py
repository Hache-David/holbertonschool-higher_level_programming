#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    int = 0
    for key in a_dictionary:
        int = a_dictionary[key] * 2
        new_dictionary.update({key: int})
    return new_dictionary
