#!/usr/bin/python3

"""
Module that contains the Function minOperations(n)
"""


def minOperations(n):
    """
    The Function minOperations(n)
    """
    if n <= 4:
        return 4
    min_op = 0
    div = 2
    while n > 1:
        while n % div == 0:
            min_op += div
            n //= div
        div += 1
    return min_op
