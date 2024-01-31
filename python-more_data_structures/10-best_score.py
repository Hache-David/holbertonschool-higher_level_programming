#!/usr/bin/python3

def best_score(a_dictionary):
    index = 0
    key_save = ""
    if a_dictionary is None or not a_dictionary:
        return None
    for key in a_dictionary:
        if abs(a_dictionary[key]) > index:
            index = a_dictionary[key]
            key_save = key
    return key_save
