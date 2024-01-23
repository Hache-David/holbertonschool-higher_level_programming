#!/usr/bin/python3
for index in range(0, 10):
    for index2 in range(0, 10):
        if index2 > index and index != 8:
            print("{}{}, ".format(index, index2), end='')
        elif index2 > index:
            print("{}{}".format(index, index2))
