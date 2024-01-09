#!/usr/bin/python3
"""
    12-pascal_triangle: pascal_triangle()
"""


def pascal_triangle(n):
    """
        returns a lis of lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """
    final_list = []
    if n <= 0:
        return final_list
    for i in range(1, n+1):
        new_row = []
        num = 1
        for j in range(1, i+1):
            new_row.append(num)
            num = num * (i - j) // j
        final_list.append(new_row)
    return final_list
