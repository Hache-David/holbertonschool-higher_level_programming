#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dictionary = dict(sorted(a_dictionary.items()))
    for key, value in dictionary.items():
        print("{}: {}".format(key, value))
