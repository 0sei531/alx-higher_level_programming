# Correcting block comment
#!/usr/bin/env python3
"""
A peak in a list is a value that is greater than or equal to its neighbors.
"""


def find_peak(list_of_integers):
    """
    Function to find a peak in a list of integers.
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]

    start, end = 0, n - 1

    while start < end:
        mid = (start + end) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
        else:
            end = mid

    return list_of_integers[start]

