#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for ligne in matrix:
        new_ligne = list(map(square, ligne))
        new_matrix.append(new_ligne)

    return new_matrix


def square(x):
    return x ** 2
