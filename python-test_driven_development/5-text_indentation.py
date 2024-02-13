#!/usr/bin/python3

'''function that prints a text with 2 new lines after each of these characters: ., ? and :'''


def text_indentation(text):
    '''core function'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for character in text:
        print(character, end='')
        if character == '.' or character == '?' or character == ':':
            print("\n")
