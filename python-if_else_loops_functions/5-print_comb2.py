#!/usr/bin/python3
for index in range(00, 100):
    if index < 10:
        print("0{}, ".format(index), end='')
    else:
        print("{}{}".format(index, ", " if index != 99 else '\n'),  end='')
