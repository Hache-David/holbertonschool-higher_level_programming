#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    string = my_list.copy()
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    string[idx] = element
    return string
