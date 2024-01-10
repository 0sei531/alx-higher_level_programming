#!/usr/bin/python3
import sys
from collections import defaultdict


def print_info(file_size, status_codes):
    print('File size: {:d}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))


# Ensure two blank lines before the function definition
status_codes = defaultdict(int)
file_size = 0

try:
    for lc, line in enumerate(sys.stdin, start=1):
        if lc % 10 == 0:
            print_info(file_size, status_codes)

        pieces = line.split()

        try:
            status = int(pieces[-2])
            status_codes[str(status)] += 1
        except (IndexError, ValueError) as e:
            # Handle unexpected input
            print(f"Skipping line {lc}: Unexpected log format - {e}")

        try:
            file_size += int(pieces[-1])
        except (IndexError, ValueError) as e:
            # Handle unexpected input
            print(f"Skipping line {lc}: Unexpected log format - {e}")

    print_info(file_size, status_codes)

except KeyboardInterrupt:
    print_info(file_size, status_codes)
    raise
