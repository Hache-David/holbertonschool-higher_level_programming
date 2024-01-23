#!/usr/bin/python3
for index in range(00, 99):
    if index < 10:
        print("0{}, ".format(index), end='')
    else:
        print("{}{}".format(index, ", " if index != 98 else '\n'),  end='')
