#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    value = 0
    for idx in range(x):
        try:
            print("{}".format(my_list[idx]), end="")
            value += 1
        except Exception as error:
            break
        print("")
        return (value)
