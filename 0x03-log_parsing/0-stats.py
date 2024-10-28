#!/usr/bin/python3
"""
0-stats.py

This script reads entries from standard input, and outputs statistics about
the total file size and the occurrence of specific HTTP status codes.
"""

import sys
import signal

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def signal_handler(sig, frame):
    """Handle keyboard interrupt and print statistics."""
    print_statistics()
    sys.exit(0)


def print_statistics():
    """Print current statistics and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

# Set the signal handler for CTRL+C


signal.signal(signal.SIGINT, signal_handler)

try:
    # Read from standard input line by line
    for line in sys.stdin:
        line_count += 1

        # Parse the log line
        parts = line.split()
        if len(parts) != 9:
            continue  # Skip lines that do not match the expected format

        # Extract relevant data
        try:
            ip_address = parts[0]
            date = parts[2][1:]  # Remove the opening bracket
            status_code = int(parts[7])
            file_size = int(parts[8])
        except (ValueError, IndexError):
            continue  # Skip lines with invalid data

        # Update total size and status codes
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
