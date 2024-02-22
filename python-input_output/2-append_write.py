#!/usr/bin/python3
'''Write a function that appends a string at the end
of a text file (UTF8) and returns the number of characters added:'''
def append_write(filename="", text=""):
    '''write file'''
    with open(filename, 'a', encoding="utf-8") as file:
        write_data = file.write(text)
    return write_data
