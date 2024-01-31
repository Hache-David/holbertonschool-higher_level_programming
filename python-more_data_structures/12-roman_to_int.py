#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dico = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    index = 0
    if roman_string is None or not roman_string:
        return 0
    for roman_letter in roman_string:
        for key in roman_dico:
            if roman_letter == key:
                index += roman_dico[key]
    return index
