#!/usr/bin/python3

"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    The function
    """

    keys = boxes[0]
    opened = [0]
    number_of_boxes = len(boxes)

    while keys:
        key = keys.pop(0)
        if key >= number_of_boxes or key < 0:
            continue
        if key not in opened:
            opened.append(key)
            for key in boxes[key]:
                keys.append(key)
    return len(opened) == number_of_boxes
