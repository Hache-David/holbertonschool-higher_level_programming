#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":


    i = 1
    if len(argv) == 2:
        print("1 argument:")
    elif len(argv) == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(argv) - 1))
    while i != len(argv):
        print("{} : {}".format(i, argv[i]))
        i += 1
