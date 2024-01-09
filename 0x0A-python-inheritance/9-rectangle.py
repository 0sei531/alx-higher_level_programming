#!/usr/bin/python3
"""Rectangle Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        """Initializates a new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Public instance method area"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of a rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
