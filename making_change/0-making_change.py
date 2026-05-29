#!/usr/bin/python3
"""Module to determine the fewest number of coins needed to meet a total."""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet total.
             If total is 0 or less, return 0.
             If total cannot be met by any combination of coins, return -1.
    """
    if total <= 0:
        return 0

    if coins is None or len(coins) == 0:
        return -1

    # Initialize DP array with a value greater than any possible solution
    # (total + 1 acts as our conceptual "infinity")
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Fill the DP table
    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    # If the total index wasn't updated, it's impossible to make change
    return dp[total] if dp[total] != total + 1 else -1
