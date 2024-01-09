#!/usr/bin/python3
""" Module that executes a function that appends a line """
import codecs

def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a string is found

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for.
        new_string (str): The string to append.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            lines = f.readlines()

        found = False
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string)
                found = True
                break

        if not found:
            raise ValueError(f"Search string '{search_string}' not found in the file.")

        with open(filename, 'w', encoding="utf-8") as f:
            f.writelines(lines)

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
