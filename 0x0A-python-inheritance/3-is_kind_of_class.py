"""Module containing is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class;
    otherwise False.
    Args:
        obj (object): Object to compare
        a_class (class): class to compare with
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
