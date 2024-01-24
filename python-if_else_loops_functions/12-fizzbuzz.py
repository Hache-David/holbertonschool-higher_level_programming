#!/usr/bin/python3

def fizzbuzz():
    int = 1
    while int < 100:
        if int % 3 == 0 and int % 5 == 0:
            print("FizzBuzz ", end='')
            int += 1
        if int % 3 == 0:
            print("Fizz ", end='')
            int += 1
        if int % 5 == 0:
            print("Buzz ", end='')
            int += 1
        else:
            print("{} ".format(int), end='')
            int += 1
