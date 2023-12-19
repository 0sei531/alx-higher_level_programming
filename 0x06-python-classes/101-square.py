#!/usr/bin/python3
class Square:
    """
    A class that defines a square by its size and position.
    """

    def __str__(self):
        """
        Returns a string representation of the square.

        The square is printed using '#' characters with
        the specified size and position.

        Returns:
            str: A string representation of the square.
        """
        rtn = ""

        if self.size == 0:
            return rtn

        for i in range(self.position[1]):
            rtn += "\n"

        for i in range(0, self.size):
            for k in range(self.position[0]):
                rtn += " "
            for j in range(self.size):
                rtn += "#"
            if i is not (self.size - 1):
                rtn += "\n"

        return rtn

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square object with
        a default size and position.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position value.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position value of a square object.

        Args:
            value (tuple): The new position value.

        Raises:
            TypeError: If the position is not
            a tuple of 2 positive integers.
            ValueError: If the position values are negative.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the square area of the object.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a '#' square according to the size value.
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
