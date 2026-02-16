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
    output_grid = grid.copy()
    good = 1
    while good > 0:
        good =0 
        too_remove  = []
        for x in range(x_shape):
            for y in range(y_shape):
                if grid[x,y] == '@' and check_adjacent(grid, x, y, x_shape, y_shape):
                    too_remove.append((x,y))
                    print(grid)
                    print()
                    good+=1
        num_rolls += len(too_remove)
        for t in too_remove:
            grid[t[0], t[1]] = '.'
    return output_grid, grid, num_rolls

def check_adjacent(grid, x, y, x_max, y_max):
    adjacent_rolls = 0
    # check only x 
    if x+1 <x_max and grid[x+1 , y] == '@':
        adjacent_rolls+=1
    if x-1 >= 0 and grid[x-1 , y] == '@':
        adjacent_rolls+=1
    
    # check only y
    if y-1 >= 0 and grid[x, y-1 ] == '@':
        adjacent_rolls+=1
    if y+1 < y_max and grid[x, y+1 ] == '@':
        adjacent_rolls+=1

    # check both x and y
    if x+1 < x_max and y+1 < y_max and grid[x+1, y+1] == '@':
        adjacent_rolls+=1
    if x-1 >= 0 and y-1 >= 0 and grid[x-1, y-1] == '@':
        adjacent_rolls+=1

    if x+1 < x_max and y-1 >= 0 and grid[x+1, y-1] == '@':
        adjacent_rolls+=1
    if x-1 >= 0 and y+1 < y_max and grid[x-1, y+1] == '@':
        adjacent_rolls+=1

    
    if adjacent_rolls <4:
        return True
    else:
        return False

if __name__ == "__main__":
    path = "input.txt"
    ogrid, grid, num_x = part1(path)
    # print(grid)
    print(num_x)