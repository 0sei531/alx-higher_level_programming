#!/usr/bin/python3
""" Module that contains a function that writes to a text file
"""


def write_file(filename="", text=""):
    """Write a string to a text file.

    Args:
        filename (str): The name of the file.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)


class MyClass:
    """A simple class."""

    def my_function(self):
        """A simple method."""
        pass


""" Example:
    >>> write_file("example.txt", "Hello, world!")
"""
