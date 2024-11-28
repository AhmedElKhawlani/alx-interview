#!/usr/bin/python3

"""
Function that returns the fewest number of coins needed to meet
a given amount total
"""


def makeChange(coins, total):
    """
    Module that contains a function that returns the fewest number
    of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)

    nbr_coins = 0

    for coin in coins:
        while total >= coin:
            nbr_coins += 1
            total -= coin
    if total == 0:
        return nbr_coins
    return -1
