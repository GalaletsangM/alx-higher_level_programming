#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in matrix:
        for j in i:
           square = [j**2 for j in x]
    return square
