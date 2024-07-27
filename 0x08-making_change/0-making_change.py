#!/usr/bin/python3
"""
This module contains a function makeChange that determines the fewest number
of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): A list of the values of the coins in your possession.
        total (int): The total amount to make with the coins.

    Returns:
        int: The fewest number of coins needed to meet the total. If the total
             is 0 or less, returns 0. If the total cannot be met by any number
             of coins you have, returns -1.
    """
    if total <= 0:
        return 0

    # Initialize the array to hold the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # It takes 0 coins to make the total 0

    # Iterate over each coin
    for coin in coins:
        for x in range(coin, total + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
