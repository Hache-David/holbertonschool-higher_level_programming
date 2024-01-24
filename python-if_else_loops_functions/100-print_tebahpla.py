#!/usr/bin/python3

int = 122
bool = True
while int != 96:
    if bool is True:
        print(chr(int), end='')
        int -= 1
        bool = False
    else:
        print(chr(int - 32), end='')
        int -= 1
        bool = True
