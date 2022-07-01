#!/usr/bin/python3
"""
Defines a function 'matrix_divided'
The function returns a divided matrix
"""


def matrix_divided(matrix, div):
    """Divide each element of a matrix by div
    Args:
        matrix (list): matrix list to divide
        div (int): the divisor

    Raises:
        TypeError: div must be a number.
        TypeError: Each row of the matrix must have the size
        TypeError: matrix must be a matrix (list of lists) of int/float
        ZeroDivisionError

    Returns:
        lists: matrix divided by div
    """

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    matrix_divided = [x[:] for x in matrix]
    for line in matrix_divided:
        if len(line) != len(matrix_divided[0]):
            raise TypeError('Each row of the matrix must be the same size')
            
        for element_index, element in enumerate(line):
            if not isinstance(element, (int, float)):
                raise TypeError(
                        "matrix must be a matrix (list of lists)"
                        " of integers/floats"
                    )

            line[element_index] = round(element/div, 2)

        return matrix_divided
