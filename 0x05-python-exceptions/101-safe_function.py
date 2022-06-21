#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely.
    Args:
        fct: the function to execute
        args: Arguments to fct.
    Returns:
        If error occurs - None
        Otherwise - the result of function call
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
