#!/usr/bin/python3
"""
Solution to the coin change problem.
"""

def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations.
        total (int): Target amount.

    Returns:
        int: Fewest number of coins needed to meet total, or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Initialize DP array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins to make 0 total

    # Process each coin
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # Return result
    return dp[total] if dp[total] != float('inf') else -1

