#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_matrix.append([i ** 2 for i in row])
    return squared_matrix
