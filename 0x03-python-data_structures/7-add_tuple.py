#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # if tuple is < 2, set missing value to 0
    # if tuple > 2, use the first two integers
    a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    b = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    c = [x + y for x, y in zip(a, b)]
    return tuple(c[0:2])
