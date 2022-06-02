#!/usr/bin/python3
def remove_char_at(str, n):
    """
    Creates a str with the character at the specified index removed
    Parameters:
    str (str): Source str
    n (int): index of char to remove
    """

    new_str = []
    for i in range(len(str)):
        if i != n:
            new_str.append(str[i])
    return ''.join(new_str)
