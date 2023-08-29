#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element
    Args:
        my-list_1 (list): The first list.
        my_list_2 (list): the second list.
        list_length (int): The number of elements to divide.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
        return (new_list)
