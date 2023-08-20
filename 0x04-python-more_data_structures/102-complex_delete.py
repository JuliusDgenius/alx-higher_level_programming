#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = a_dictionary.copy()
    for k, l in tmp.items():
        if value == l:
            a_dictionary.pop(k)
    return a_dictionary
