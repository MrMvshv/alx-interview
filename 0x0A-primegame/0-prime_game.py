#!/usr/bin/python3
"""
Prime game module
"""


def is_prime(num):
    """
    Returns True if num is prime
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def calculate_winner(nums):
    """
    calculate winner of prime game
    """
    n = max(nums)
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    dp = [False] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = not any(dp[i - p] for p in primes if p <= i)

    return dp


def isWinner(x, nums):
    """
    main function to return winner
    """
    winners = calculate_winner(nums)
    maria_wins = 0
    ben_wins = 0

    for winner in winners:
        if winner:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
