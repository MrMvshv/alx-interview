#!/usr/bin/python3
"""
method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
more info in README
"""


def minOperations(n):
    """
    Returns an integer
    If n is impossible to achieve,
    return 0
    """
    if n <= 1:
        return 0

    operations = 0
    div = 2

    while div <= n:
        if n % div == 0:
            operations += div
            n = n // div
            div -= 1
        div += 1

    return operations
