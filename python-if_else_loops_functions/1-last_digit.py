#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = number
if number < 0:
    number = number % -10
if number > 0:
    number = number % 10
if number > 5:
    print(f"Last digit of {number2} is {number} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number2} is 0 and is 0")
elif number < 6:
    print(f"Last digit of {number2} is {number} and is less than 6 and not 0")
