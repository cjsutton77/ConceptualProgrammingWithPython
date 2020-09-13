def sp(x,y,count,grid):
    #global grid
    X = len(grid[0])
    Y = len(grid)
    
    if x == X - 1 and y == Y - 1:
        return count + 1
    grid[y][x] = 1

    # up
    if ((y >= 1 and y <= Y-1) and (x >= 1 and x <= X-2)) and grid[y-1][x] == 0:
        count = sp(x,y-1,count,grid)
    # down
    if ((y >= 0 and y <= Y-2) and (x >= 0 and x <= X-1)) and grid[y+1][x] == 0:
        count = sp(x,y+1,count,grid)
    # right
    if ((y >= 0 and y <= Y-1) and (x >= 0 and x <= X-2)) and grid[y][x+1] == 0:
        count = sp(x+1,y,count,grid)
    # left
    if ((y > 0 and y < Y-1) and (x >= 1 and x <= X-1)) and grid[y][x-1] == 0:
        count = sp(x-1,y,count,grid)

    grid[y][x] = 0
    return count

grid = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

num = sp(0,0,0,grid)
print(f'Number of solutions is {num}')