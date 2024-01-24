#!/usr/bin/python3

int = 122
bool = True
while int != 96:
    if bool is True:
        bool = False
    else:
        bool = True
    print("{}".format(chr(int) if bool is True else chr(int - 32)), end='')
    int -= 1
