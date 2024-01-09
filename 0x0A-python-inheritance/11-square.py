#!/usr/bin/python3
"""Square Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size):
        """Initializates a Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of a square"""
        return super().area()

    def __str__(self):
        """String representation of a Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
