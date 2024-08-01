#!/usr/bin/python3
'''
The Islang Perimeter Problem
'''


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid."""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Check if the cell is land
                # Check each side of the land cell
                # Top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
