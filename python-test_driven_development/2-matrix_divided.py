#!/usr/bin/python3

'''divides all elements of a matrix'''


def matrix_divided(matrix, div):
    '''core function'''
    new_matrix = [ligne[:] for ligne in matrix]
    len_first_line = len(matrix[0])

    if matrix == []:
        return matrix
    for ligne in matrix:
        if len(ligne) != len_first_line:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int or float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            if not (isinstance(new_matrix[i][j], int) or isinstance(new_matrix[i][j], float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)

    return new_matrix
