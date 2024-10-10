#!/usr/bin/python3

"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you. Each box is numbered
    sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
    """

    keys = boxes[0]
    opened = [0]
    number_of_boxes = len(boxes)

    while keys:
        key = keys.pop(0)
        if key >= number_of_boxes:
            continue
        if not key in opened:
            opened.append(key)
            for key in boxes[key]:
                keys.append(key)
    return len(opened) == number_of_boxes
