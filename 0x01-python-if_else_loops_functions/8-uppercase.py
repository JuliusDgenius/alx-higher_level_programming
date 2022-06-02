#!/usr/bin/python3
def uppercase(str):
    """
    Prints a str, convert lowercase to uppercase
    Parameters:
    str (str): String to print
    """
    txt = ''.join(str) + '\n'
    for i in range(len(txt)):
        c = ord(txt[i])
        is_lower = (c >= ord('a')) and (c <= ord('z'))
        offset = (1 << 5) if is_lower else 0
        print('{:c}'.format(c - offset), end='')
