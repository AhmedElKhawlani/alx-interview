#!/usr/bin/python3
"""
Prime Game Solution
This script defines a solution to determine the winner of the Prime Game.
"""


def generate_primes(n):
    """
    Generate a list of prime numbers from 1 to n (inclusive).
    """
    primes_list = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes_list.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return primes_list


def is_winner(rounds, nums):
    """
    Determine the winner of the Prime Game.
    """
    if not rounds or not nums or rounds == 0 or not nums:
        return None

    maria_score = 0
    ben_score = 0

    for i in range(rounds):
        primes_list = generate_primes(nums[i])
        if len(primes_list) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    return None
