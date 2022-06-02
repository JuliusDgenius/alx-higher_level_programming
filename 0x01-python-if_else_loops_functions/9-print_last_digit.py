#!/usr/bin/python3
def print_last_digit(number):
    """
    Printd the last digit of a number and returns its value
    Parameters:
    number (int): number
    """
    print('{:c}'.format((abs(int(number)) % 10) + ord('0')), end='')
    return abs(int(number)) % 10
