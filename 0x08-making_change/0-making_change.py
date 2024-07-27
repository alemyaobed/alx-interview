#!/usr/bin/python3

def makeChange(coins, total):
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
