#!/usr/bin/python3
"""Add Attribute Module"""


def add_attribute(obj, attribute, value):
    """Function that adds a new attribute to an object if it’s possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
