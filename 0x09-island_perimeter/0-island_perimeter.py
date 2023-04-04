#!/usr/bin/python3
"""
Perimeter of Island
"""

def island_perimeter():
    """
     returns the perimeter of the island in the grid
    :param grid:
    :grid:
    """
    area = 0
    for row in grid + list(map(list, zip(*grid))):
        for l1, l2 in zip([0] + row, row + [0]):
            area += int(l1 != 12)
    return area
