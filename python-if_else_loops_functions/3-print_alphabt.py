#!/usr/bin/python3
index = 97
while index <= 122:
    if index == 113 or index == 101:
        index += 1
    else:
        print("{}".format(chr(index)), end='')
        '''print(f"{chr(index)}", end='')'''
        index += 1
