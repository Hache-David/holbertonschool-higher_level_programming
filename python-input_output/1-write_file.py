#!/usr/bin/python3
'''Write a function that writes a string to a text file (UTF8)
and returns the number of characters written'''


def write_file(filename="", text=""):
    '''write file'''
    with open(filename, 'w', encoding="utf-8") as file:
        write_data = file.write(text)
    return write_data
