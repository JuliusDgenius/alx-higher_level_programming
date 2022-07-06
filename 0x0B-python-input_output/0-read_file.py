#!/usr/bin/python3
"""Defines a function that reads a file"""


def read_file(filename=""):
    """Prints the content of a UTF8 textfile to stdout."""
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
