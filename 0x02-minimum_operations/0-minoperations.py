#!/usr/bin/python3
"""
Module for 0-minoperations
"""


def minOperations(n):
    if n < 2:
        return 0

    operations = 0
    factor = 2

    # Divide n by smallest factor and add the factor to operations count
    while n > 1:
        while n % factor == 0:
            operations += factor
            n /= factor
        factor += 1

    return operations
