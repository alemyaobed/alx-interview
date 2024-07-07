#!/usr/bin/python3
'''
The N queens puzzle is the challenge of placing N non-attacking queens on
an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments, print
Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line,
and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line,
and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
Read: Queen, Backtracking
'''
import sys


def print_usage_and_exit():
    """Prints the usage message and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def print_invalid_number_and_exit():
    """Prints the invalid number message and exits with status 1"""
    print("N must be a number")
    sys.exit(1)


def print_too_small_and_exit():
    """Prints the too small number message and exits with status 1."""
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board, row, col):
    """
    Checks if a queen can be placed on board at (row, col) without
    being attacked.

    Args:
        board (list): 2D list representing the chessboard
        row (int): Row index
        col (int): Column index

    Returns:
        bool: True if safe, False otherwise
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col):
    """
    Utilizes backtracking to find one solution to the N Queens problem.

    Args:
        board (list): 2D list representing the chessboard
        col (int): Current column index

    Returns:
        bool: True if a solution is found, False otherwise
    """
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_nqueens_util(board, col + 1):
                return True
            board[i][col] = 0

    return False


def solve_nqueens(N):
    """
    Solves the N Queens problem and returns all possible solutions.

    Args:
        N (int): Size of the chessboard (N x N)

    Returns:
        list: List of solutions, where each solution is a list of queen
        positions
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_recursively(board, 0, solutions)
    return solutions


def solve_nqueens_recursively(board, col, solutions):
    """
    Recursively finds all solutions to the N Queens problem using backtracking.

    Args:
        board (list): 2D list representing the chessboard
        col (int): Current column index
        solutions (list): List to store all solutions

    Returns:
        bool: True if at least one solution is found, False otherwise
    """
    N = len(board)
    if col == N:
        solutions.append(board_to_positions(board))
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_recursively(board, col + 1, solutions) or res
            board[i][col] = 0

    return res


def board_to_positions(board):
    """
    Converts the board representation to a list of queen positions.

    Args:
        board (list): 2D list representing the chessboard

    Returns:
        list: List of queen positions
    """
    positions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                positions.append([i, j])
    return positions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_invalid_number_and_exit()

    if N < 4:
        print_too_small_and_exit()

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
