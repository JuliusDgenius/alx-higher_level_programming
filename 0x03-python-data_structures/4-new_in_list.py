#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return
    else:
        new_copy = my_list.copy()
        if (0 <= idx < len(my_list)):
            new_copy[idx] = element
        return new_list
