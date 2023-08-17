#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp = my_dict.copy
    for j, k in tmp.items():
        if value == k:
            my_dict.pop(k)
    return my_dict
