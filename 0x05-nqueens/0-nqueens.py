#!/usr/bin/python3
"""
N Queens Problem Solver

This script solves the N Queens problem using a backtracking algorithm.
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    Queens must not share the same column or diagonal.
    """
    for i in range(row):
        # Check if there is a queen in the same column or on either diagonal
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    """
    Solve the N Queens problem and print all solutions.
    Each solution is a list of lists, where each list contains
    the row and column of a queen.
    """
    def backtrack(row=0):
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Reset the row after backtracking

    solutions = []
    board = [-1] * N
    backtrack()
    return solutions

def print_solutions(solutions):
    """
    Print each solution in the specified format.
    """
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    # Validate command-line input
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve and print all solutions
    solutions = solve_nqueens(N)
    print_solutions(solutions)
