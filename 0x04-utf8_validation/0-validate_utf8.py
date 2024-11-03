#!/usr/bin/python3

"""
Module that defines a Function that that determines if a given data set
represents a valid UTF-8 encoding
"""


def retrieve_leading_set_bits(num):
    """
    Function that returns the number of leading set bits
    This function can be used in validUTF8(data)
    """
    leading_set_bits_count = 0
    mask = 1 << 7
    while mask & num:
        leading_set_bits_count += 1
        mask >>= 1
    return leading_set_bits_count


def validUTF8(data):
    """
    Function that that determines if a given data set
    represents a valid UTF-8 encoding
    """
    bits_count = 0
    for i in range(len(data)):
        if bits_count == 0:
            bits_count = retrieve_leading_set_bits(data[i])
            if bits_count == 0:
                continue
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bits_count -= 1
    return bits_count == 0
