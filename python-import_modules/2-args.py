#!/usr/bin/python3
import sys

i = 1
if len(sys.argv) == 2:
    print("1 argument:")
elif len(sys.argv) == 1:
    print("0 arguments.".format(len(sys.argv) - 1))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
while i != len(sys.argv):
    print("{} : {}".format(i, sys.argv[i]))
    i += 1
