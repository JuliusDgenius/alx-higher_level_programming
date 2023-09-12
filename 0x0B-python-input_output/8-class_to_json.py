#!/usr/bin/python3
"""Defines a function that defines a Python class-to-JSON."""


def class_to_json(obj):
    """Returns the dictionary representation of a simpledata structure"""
    return obj.__dict__
