#!/usr/bin/python3
""" Module that contains utility functions for working with JSON files
"""
import json
import os.path


def from_json_string(my_str):
    """ Return a Python object from a JSON representation.

    Args:
        my_str (str): The JSON representation string.

    Returns:
        obj: The Python object represented by the JSON string.
    """
    return json.loads(my_str)


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


def load_from_json_file(filename):
    """ Load a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        obj: The Python object loaded from the JSON file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)


def add_items_to_list_and_save():
    """ Add command-line arguments to a Python list and save it to a JSON file.
    """
    import sys

    # Load existing data from the JSON file
    my_list = []
    if os.path.exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")

    # Add command-line arguments to the list
    for arg in sys.argv[1:]:
        my_list.append(arg)

    # Save the updated list to the JSON file
    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    add_items_to_list_and_save()
