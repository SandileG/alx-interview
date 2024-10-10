#/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    Returns a list of lists of integers representing Pascal’s triangle of n.
    """
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate rows 2 to n
    for i in range(1, n):
        # Start each row with a 1
        row = [1]
        # Each number (except the first and last) is the sum of the two numbers above it
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with a 1
        row.append(1)
        # Append the row to the triangle
        triangle.append(row)

    return triangle
