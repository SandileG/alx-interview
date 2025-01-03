#!/usr/bin/python3
"""
Main file for testing the makeChange function.
"""

makeChange = __import__('0-making_change').makeChange

# Test cases
print(makeChange([1, 2, 25], 37))  # Expected output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
