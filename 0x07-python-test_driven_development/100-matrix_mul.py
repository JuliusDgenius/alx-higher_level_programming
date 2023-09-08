#!/usr/bin/python3
"""This module defines 'the matrix_mul' function to multiply 2 matrices
"""


def matrix_mul(m_a, m_b):
    """This function multiplies 2 matrices and returns the their product
    Args:
        m_a = The first matrix
        m_b = The second matrix
    """
    result = [[sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
               for j in range(len(m_b[0]))] for i in range(len(m_a))]
    return result
