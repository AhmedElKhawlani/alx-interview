#!/usr/bin/python3

"""
This module contain the function island_perimeter
"""


def island_perimeter(grid):
    """
    This funtion Returns the perimeter of the island represented by grid
    """
    lines = len(grid)
    columns = len(grid[0])
    perimeter = 0
    for i in range(lines):
        for j in range(columns):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if i == lines - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == columns - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
