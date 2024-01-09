#!/usr/bin/python3
class MyList(list):
    """Class that inherits the attributes and methods of the list class.

     Args:
        list: The built-in list class.
    """

    def print_sorted(self):
        """Method that prints the sorted list."""
        print(sorted(self))
