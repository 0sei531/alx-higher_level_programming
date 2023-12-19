#!/usr/bin/python3
class Square:
    """
    A class that defines a square by its size.
    """

    def __eq__(self, other):
        """
        Checks if the size of the square is
        equal to the size of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if sizes are equal, False otherwise.
        """
        return self.__size == other.__size

    def __lt__(self, other):
        """
        Checks if the size of the square is
        less than the size of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the size is less, False otherwise.
        """
        return self.__size < other.__size

    def __le__(self, other):
        """
        Checks if the size of the square is less
        than or equal to the size of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the size is less than or equal, False otherwise.
        """
        return self.__size <= other.__size

    def __ne__(self, other):
        """
        Checks if the size of the square is
        not equal to the size of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if sizes are not equal, False otherwise.
        """
        return self.__size != other.__size

    def __gt__(self, other):
        """
        Checks if the size of the square is
        greater than the size of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the size is greater, False otherwise.
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """
        Checks if the size of the square is greater
        than or equal to the size of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the size is greater than or equal, False otherwise.
        """
        return self.__size >= other.__size

    def __init__(self, size=0):
        """
        Initializes the square object with a default size.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Retrieves the size value.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size value of the square object.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
