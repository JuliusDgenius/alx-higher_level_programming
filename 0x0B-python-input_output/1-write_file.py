#!/usr/bin/python3
"""Defines a function that writes into a file"""


def write_file(filename="", text=""):
    """writes a sring to UTF* text file"""

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
