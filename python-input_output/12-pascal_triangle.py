#!/usr/bin/python3
'''Create a function def pascal_triangle(n): that returns a
list of lists of integers representing the
Pascal’s triangle of n:'''


def pascal_triangle(n):
    new_list = [[1]]
    if n <= 0:
        return new_list
    for number in range(1, n):
        new_list2 = [1]
        for number2 in range(1, number):
            new_list2.append(
                new_list[number-1][number2-1] + new_list[number-1][number2])
        new_list2.append(1)
        new_list.append(new_list2)
    return new_list
