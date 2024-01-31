#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for int in my_list:
        if int == search:
            int = replace
        new_list.append(int)
    return new_list
