#!/usr/bin/python3
"""My Int Module"""


class MyInt(int):
    """MyInt Class"""
    def __eq__(self, other):
        """Invert operator == by !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert operator != by =="""
        return super().__eq__(other)
