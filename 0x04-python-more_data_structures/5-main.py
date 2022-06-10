#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
num_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(num_keys))
