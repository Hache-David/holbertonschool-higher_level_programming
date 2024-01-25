#!/usr/bin/python3

def remove_char_at(str, n):
    i = 0
    str2 = ""
    for char in str:
        if i == n:
            i += 1
            continue
        else:
            i += 1
            print(char, end='')
    return ""
