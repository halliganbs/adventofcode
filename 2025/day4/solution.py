import numpy as np

def make_grid(path):
    with open(path) as f:
        lines = f.read().splitlines()
    x_shape = len(lines)
    y_shape = len(lines[0])
    grid = np.empty((x_shape, y_shape), dtype=str)
    for i, l in enumerate(lines):
        for j, val in enumerate(l):
            grid[i, j] = val
    return grid, x_shape, y_shape

def part1(path):
    num_rolls = 0
    grid, x_shape, y_shape = make_grid(path)
    for x in range(x_shape):
        for y in range(y_shape):
            if grid[x,y] == '@' and check_adjacent(grid, x, y, x_shape, y_shape):
                grid[x,y] = 'x'
                num_rolls+=1
    return grid, num_rolls

def check_adjacent(grid, x, y, x_max, y_max):
    adjacent_rolls = 0
    # check x+1 
    if grid[x+1, y] == '@':
        adjacent_rolls+=1
    if grid[x-1, y] == '@':
        adjacent_rolls+=1
    if grid[x, y-1] == '@':
        adjacent_rolls+=1
    if grid[x, y+1] == '@':
        adjacent_rolls+=1

    
    if adjacent_rolls < 4:
        return True
    else:
        return False

if __name__ == "__main__":
    path = "test.txt"
    print(part1(path))