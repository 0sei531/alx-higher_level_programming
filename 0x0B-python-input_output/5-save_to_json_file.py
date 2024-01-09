#!/usr/bin/python3
""" Module that writes an object to a
text file using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Write an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be written.
        filename (str): The name of the text file.

    Raises:
        Exception: If the object can't be encoded to JSON.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
