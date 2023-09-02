#!/usr/bin/python3
"""
This is the '2-matrix_divided' module.

The module supplies the function, 'matrix_divided(matrix, div)' which \
        divides each memmer of a matrix of list of lists of integers by a \
        given number
"""


def matrix_divided(matrix, div):
    """Divides a list of lists of integers by a given number
    Args:
        matrix (list): A list of lists of integer.
        div (int): The divisor to divide each integer member of list
        Return: Returns a list of list of the result.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
    size = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
                    of integers/floats")
    if size is None:
        size = len(row)
    elif size != len(row):
        raise TypeError("Each row of the matrix must have the same size")
    for integer in row:
        if type(integer) is not int and type(integer) is not float:
            raise TypeError("matrix must be a matrix of (list of lists) \
                    of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(integer / div, 2) for integer in row] for row in matrix]
