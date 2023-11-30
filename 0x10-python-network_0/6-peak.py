#!/usr/bin/python3
# Function that finds a peak in a list of unsorted integers

def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    else:
        s = sorted(list_of_integers)
    return s[-1]
