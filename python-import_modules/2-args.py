#!/usr/bin/python3
import sys
i = 1
print("{} arguments.".format(len(sys.argv) - 1))
while i != len(sys.argv):
    print("{} : {}".format(i, sys.argv[i]))
    i += 1
