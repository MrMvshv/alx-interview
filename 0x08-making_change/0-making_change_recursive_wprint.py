#!/usr/bin/python3
"""
Given a pile of coins of different values
determine the fewest number of coins needed
to meet a given amount total.
"""
def makeChangeRecursive(coins, total, change=0, n=0):
    """recursive function that makes change"""
    print(f"recursive run({n}):\n coins: {coins}, total: {total}, change: {change}")
    n += 1
    if total <= 0:
        return 0

    if len(coins) == 0:
        return -1

    div = max(coins)
    print(f"div: {div}")
    
    if total >= div:
        change_for_div = total // div
        print(f"change for {div}: {change_for_div}")
        remaining_total = total % div
        print(f"remaining total: {remaining_total}")
        return change_for_div + makeChangeRecursive(coins, remaining_total, change + change_for_div, n)

    coins.remove(div)
    return makeChangeRecursive(coins, total, change, n)

def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
            If total is 0 or less, 0
            If total cannot be met by any number of coins ,-1
    """
    result = makeChangeRecursive(coins, total, 0)
    if (len(coins) == 0) and total > 0:
        return -1
    return result
