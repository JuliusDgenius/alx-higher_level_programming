#!/usr/bin/python3


def print_list_integer(my_list=[]):
    i = 0
    if my_list == "":
        return ("No elements found")
    else:
        for i in range(len(my_list)):
            print("{:d}\n".format(my_list[i]))
