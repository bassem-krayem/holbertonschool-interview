#!/usr/bin/python3
"""
    A script that reads stdin line by line and computes metrics
    about HTTP status codes and the total file size.
    It outputs the total file size and counts of various HTTP
    status codes (200, 301, 400, 401, 403, 404, 405, and 500)
    in a sorted order.
"""
import sys


def print_msg(codes, file_size):
    """
    A function that prints the
    computed metrics (file size and status code counts)

    Args:
        codes (dict): A dictionary with status
        codes as keys and counts as values.
        file_size (int): The total size of files processed.
    """
    # Print the total file size
    print("File size: {}".format(file_size))

    # Print each HTTP status code and its count (only if count is not 0)
    for key, val in sorted(codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


# Initialize variables to store file size, code counts, and line count
file_size = 0
code = 0
count_lines = 0

# Define a dictionary to track the count of specific HTTP status codes
codes = {
    "200": 0,  # OK
    "301": 0,  # Moved Permanently
    "400": 0,  # Bad Request
    "401": 0,  # Unauthorized
    "403": 0,  # Forbidden
    "404": 0,  # Not Found
    "405": 0,  # Method Not Allowed
    "500": 0   # Internal Server Error
}

try:
    # Read each line from stdin
    for line in sys.stdin:
        # Split the line and reverse it (file size is first, code is second)
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        # Check if there are enough elements in the line (file size and status
        if len(parsed_line) > 2:
            count_lines += 1  # Count the number of lines processed

            if count_lines <= 10:
                # Add the file size from the line to the total
                file_size += int(parsed_line[0])
                # Extract the HTTP status code from the line
                code = parsed_line[1]

                # If the code is a valid HTTP status code, increment its count
                if code in codes.keys():
                    codes[code] += 1

            # After processing 10 lines, print the metrics and reset
            if count_lines == 10:
                print_msg(codes, file_size)
                count_lines = 0

finally:
    # Print the final metrics (even if there are fewer than 10 lines processed)
    print_msg(codes, file_size)
