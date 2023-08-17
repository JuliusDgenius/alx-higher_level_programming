#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        list_keys = list(a_dictionary.keys())
        list_keys.sort()
        for key in list_keys:
            print("{}: {}".format(key, a_dictionary.get(key)))
