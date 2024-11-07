#!/usr/bin/python3
"""
N-Queens Problem Solver
"""
import sys


def solve_nqueens(row, n, cols, pos_diagonals, neg_diagonals, board):
    """
    Recursive function to solve the N-Queens problem using backtracking.
    """
    if row == n:
        solution = [[r, c] for r in range(n) for c in range(n)
                    if board[r][c] == 1]
        print(solution)
        return

    for col in range(n):
        con1 = col in cols or (row + col) in pos_diagonals
        con2 = (row - col) in neg_diagonals
        if con1 or con2:
            continue

        cols.add(col)
        pos_diagonals.add(row + col)
        neg_diagonals.add(row - col)
        board[row][col] = 1

        solve_nqueens(row + 1, n, cols, pos_diagonals, neg_diagonals, board)

        cols.remove(col)
        pos_diagonals.remove(row + col)
        neg_diagonals.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Solves the N-Queens problem.

    Args:
        n (int): The number of queens. Must be at least 4.

    Returns:
        None
    """
    board = [[0] * n for _ in range(n)]
    solve_nqueens(0, n, set(), set(), set(), board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
