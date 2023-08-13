#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_copy = []

    if idx < 0 or idx > len(my_list):
        return my_list

    for i in my_list:
        new_copy.append(i)

    for i in new_copy:
        if i == idx:
            new_copy[i] = element
    return new_copy
