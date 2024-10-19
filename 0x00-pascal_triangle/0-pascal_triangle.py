#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
    list of lists: A list of lists

    Pascal's Triangle follows this structure:
    - The first and last element of each row are 1.
    - Each inner element of a row is the sum of the two lists
    """

    # Return an empty list if n <= 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row, which is always [1]
    triangle = [[1]]

    # Generate rows 2 to n
    for i in range(1, n):
        # Start each new row with a 1
        row = [1]

        # Populate the row with sums of adjacent values from the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # End each row with a 1
        row.append(1)

        # Append the new row to the triangle
        triangle.append(row)

    return triangle
