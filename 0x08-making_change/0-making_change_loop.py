#!/usr/bin/python3
"""
Given a pile of coins of different values
determine the fewest number of coins needed
to meet a given amount total.
"""
def calc():
    """
    divide, return remainder
    """
    return 0

def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
            If total is 0 or less, 0
            If total cannot be met by any number of coins ,-1
    """
    change = 0

    while (len(coins) > 0):
        div = max(coins)
        print(f"div: {div}")
        if (total > div):
            change += (total // div)
            print(f"change: {change}")
            total = total % div
            print(f"total: {total}")
        coins.remove(div)
    if total > 0:
        return -1
    return change
