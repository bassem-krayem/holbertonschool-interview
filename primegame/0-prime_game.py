#!/usr/bin/python3
"""
Module for the Prime Game.
Determines the winner after x rounds of picking primes and their multiples.
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): Number of rounds.
        nums (list): Array of n values for each round.

    Returns:
        str: Name of the player who won the most rounds ("Maria" or "Ben").
        None: If the winner cannot be determined (tie) or invalid inputs.
    """
    if not nums or x < 1:
        return None

    # Find the maximum value of n to dynamically scale our sieve limit
    max_n = max(nums)

    # 1. Sieve of Eratosthenes to precompute primes up to max_n
    # True indicates a prime, False indicates non-prime
    sieve = [True] * (max_n + 1)
    if max_n >= 0:
        sieve[0] = False
    if max_n >= 1:
        sieve[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # 2. Cumulative count of primes up to each index i
    # This lets us know exactly how many prime turns occur in O(1) time
    prime_counts = [0] * (max_n + 1)
    count = 0
    for i in range(len(sieve)):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    # 3. Simulate rounds using the precomputed prime counts
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Get the number of primes up to n
        primes_available = prime_counts[n]
        # If odd number of primes, Maria wins. If even, Ben wins.
        if primes_available % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    # 4. Determine final match winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
