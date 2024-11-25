# Rotating a 2D Matrix by 90 Degrees Clockwise

## Overview

The goal of this project is to implement an **in-place algorithm** to rotate an \( n \times n \) 2D matrix by **90 degrees clockwise**. This requires manipulating the given matrix directly without creating additional data structures, which helps improve space efficiency. 

This README will walk you through the essential concepts and techniques you'll need to master for successful implementation.

---

## Key Concepts

### 1. **Matrix Representation in Python**

In Python, a 2D matrix is represented as a **list of lists**, where each inner list represents a row of the matrix. For example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

#### Accessing Elements
- To access the element at the first row and second column (`matrix[0][1]`):  
  ```python
  print(matrix[0][1])  # Output: 2
  ```

#### Modifying Elements
- You can modify the value of an element by directly assigning a new value:  
  ```python
  matrix[1][2] = 10
  print(matrix)
  # Output: [[1, 2, 3], [4, 5, 10], [7, 8, 9]]
  ```

---

### 2. **In-place Operations**

An **in-place operation** modifies the data structure directly without using additional memory for a duplicate. This is crucial in scenarios where memory usage must be minimized. For this project:
- You must rotate the matrix without creating a new matrix.
- This is achieved by performing operations directly on the existing matrix.

**Advantages:**
- Saves memory.
- Reduces the overhead of copying large data structures.

---

### 3. **Matrix Transposition**

**Matrix transposition** involves swapping the rows and columns of a matrix.  
For example, transposing the matrix:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Results in:

```python
transposed = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

#### Implementation
To transpose a matrix in-place:
- Swap each element at position `(i, j)` with the element at `(j, i)`.
- Iterate only through the upper triangle of the matrix to avoid overwriting:

```python
n = len(matrix)
for i in range(n):
    for j in range(i + 1, n):  # Avoid redundant swaps
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

---

### 4. **Reversing Rows**

After transposing the matrix, you need to **reverse each row** to achieve a 90-degree clockwise rotation. For example:

```python
transposed = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

Reversing each row results in:

```python
rotated = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

#### Implementation
Reversing a row can be done using slicing:

```python
for row in matrix:
    row.reverse()
```

Alternatively, use slicing syntax for the same result:

```python
for i in range(len(matrix)):
    matrix[i] = matrix[i][::-1]
```

---

### 5. **Nested Loops for 2D Matrix Manipulation**

When working with 2D matrices, **nested loops** are essential. These allow you to iterate over rows and columns systematically. For example:

```python
n = len(matrix)
for i in range(n):
    for j in range(n):
        print(matrix[i][j])  # Access element at row i, column j
```

Nested loops are critical for:
- Transposing the matrix.
- Reversing rows.
- Implementing in-place modifications.

---

## Algorithm for Rotating a 2D Matrix

To rotate an \( n \times n \) matrix by 90 degrees clockwise:
1. **Transpose the matrix**: Swap elements at `(i, j)` with `(j, i)`.
2. **Reverse each row**: Reverse the order of elements in each row.

### Step-by-Step Example

Input Matrix:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Step 1: Transpose the Matrix**
```python
matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

**Step 2: Reverse Each Row**
```python
matrix = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

---

## Final Implementation

Here is the complete implementation of the rotation algorithm:

```python
def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise in place."""
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
```

---

## Summary

To successfully rotate a 2D matrix by 90 degrees clockwise:
1. Understand the basics of matrix representation and manipulation in Python.
2. Learn the concepts of transposing and reversing rows.
3. Use in-place operations to minimize space complexity.
4. Practice implementing these steps using nested loops.
