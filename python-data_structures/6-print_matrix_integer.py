#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    taille = 0
    for ligne in matrix:
        taille = len(ligne) - 1
        for int in ligne:
            print("{}".format(int), end="")
            if int != ligne[taille]:
                print(" ", end="")
        print()
