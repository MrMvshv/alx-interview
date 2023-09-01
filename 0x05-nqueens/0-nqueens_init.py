#!/usr/bin/python3
"""N queens puzzle"""
import sys


def is_safe(board, row, col, N):
    """Check if there is a queen in the same column on any previous rows"""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def chessputer(N):
    """computes options"""
    def backtrack(row):
        if row == N:
            solutions.append(list(enumerate(board)))
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1)

    solutions = []
    board = [-1] * N
    backtrack(0)
    return solutions


def printA(option):
    """prints it"""
    for row in option:
        print(f"[{row[0]}, {row[1]}]", end=" ")
    print()


def start():
    """entry point of program"""
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

    options = chessputer(N)
    for option in options:
        printA(option)
        print()


if __name__ == "__main__":
    start()
