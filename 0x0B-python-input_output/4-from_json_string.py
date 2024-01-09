#!/usr/bin/python3
""" Module that contains a function to return
an object from a JSON representation

"""
import json


def from_json_string(my_str):
    """ Return a Python object from a JSON representation.

    Args:
        my_str (str): The JSON representation string.

    Returns:
        obj: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
