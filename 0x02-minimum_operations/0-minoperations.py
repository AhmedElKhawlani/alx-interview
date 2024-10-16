#!/usr/bin/python3

"""
Module that contains the Function minOperations(n)
"""


def minOperations(n):
    """
    The Function minOperations(n)
    """
    L = [0, 1, 2, 3, 4]
    for i in range(5, n + 1):
        L.append(min(1 + L[i - 1], 2 + L[i // 2]))
    return L[n]
