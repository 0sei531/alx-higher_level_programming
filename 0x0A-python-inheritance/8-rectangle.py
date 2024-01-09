#!/usr/bin/python3
"""Rectangle Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
     """Rectangle Class"""
     def __init__(self, width, height):
         """Initializes a new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

     def __str__(self):
         """String representation of the rectangle"""
         return "[Rectangle] {}/{}".format(self.__width, self.__height)
