import numpy as np


def possible(x, y, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid), end='\n\n')


if __name__ == "__main__":
    grid = [[2, 0, 0, 3, 6, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 3, 0],
            [0, 0, 3, 2, 4, 0, 0, 9, 0],
            [0, 2, 7, 0, 0, 0, 0, 1, 0],
            [0, 3, 1, 6, 0, 0, 9, 0, 0],
            [6, 0, 9, 8, 1, 0, 2, 0, 7],
            [9, 6, 2, 4, 0, 0, 3, 0, 0],
            [1, 0, 5, 0, 3, 0, 4, 2, 0],
            [3, 7, 4, 0, 8, 2, 5, 6, 0], ]
    solve()
