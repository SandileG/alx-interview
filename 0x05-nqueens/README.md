## N Queens

## Project Overview

The goal of the "N Queens" project is to place N queens on an N×N chessboard so that no two queens attack each other. This involves understanding and implementing a backtracking algorithm, a key technique for solving constraint-based problems efficiently.

# Key Concepts

# 1. Backtracking Algorithm
Backtracking explores potential solutions by attempting to build them piece by piece. If a partial solution cannot be completed, the algorithm "backtracks" to try a different approach.

Steps:
Place a queen on the board one row at a time.
For each queen placement, check if it conflicts with any previously placed queens.
If no conflict, proceed to the next row.
If a conflict is detected, remove (backtrack) the last queen placed and try a new position.

# 2.  Recursion in Python
Recursion is essential for backtracking, as it allows the function to "call itself" for each row in the chessboard.

Recursive Function: The function will attempt to place queens one at a time and call itself for the next row, exploring all possible queen placements.

# 3. List Manipulation in Python
The N queens solution requires storing each queen’s position. You’ll use lists to keep track of queen placements and manipulate them as you backtrack.

Position Storage: Use a list where each index represents a row, and the value at each index represents the column position of the queen.

# 4. Handling Command-Line Arguments
The N queens program will accept N as a command-line argument, which specifies the size of the board and the number of queens.

Command-Line Parsing: Use the sys module to retrieve command-line arguments, ensuring that N is a valid integer.
Implementation Outline
Here's a high-level outline to help you structure your solution:

# Define a Helper Function:

Create a function to check if placing a queen at a given row and column is safe.
The function should ensure no queens are in the same column, or on the same diagonal.
Define the Backtracking Function:

Use recursion to try placing a queen in each row.
Store positions as you go, backtracking when a conflict occurs.
If all queens are placed successfully, save the solution.
Use Command-Line Input:

Use sys.argv to accept N as an input from the command line.
