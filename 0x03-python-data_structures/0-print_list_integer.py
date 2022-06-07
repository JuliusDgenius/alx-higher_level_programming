#!/usr/bin/python3


def print_list_integer(my_list=[]):
    i = 0
    for i in range(len(my_list)):
            if my_list[i] == "H":
                continue
            else:
                print("{:d}\n".format(my_list[i]))
