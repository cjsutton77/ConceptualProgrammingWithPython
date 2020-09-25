#!/usr/bin/env python
# coding: utf-8

# In[1]:


grid = [[0 for i in range(8)] for j in range(8)]


# In[2]:


def place(row,col,grid,val=1):
    grid[row][col] = 99
    for i in range(8):
        if grid[i][col] != 99:
            grid[i][col] = grid[i][col]+val
        else:
            continue
    for j in range(8):
        if grid[row][j] != 99:
            grid[row][j] = grid[row][j]+val
        else:
            continue
    # upper left
    for i in range(1,7):
        x = row - i
        y = col - i
        if x >= 0 and y >= 0:
            grid[x][y] = grid[x][y]+val
        else:
            continue
    # upper right
    for i in range(1,7):
        x = row + i
        y = col - i
        if x <= 7 and y >= 0:
            grid[x][y] = grid[x][y]+val
        else:
            continue    
    # lower left
    for i in range(1,7):
        x = row - i
        y = col + i
        if x >= 0 and y <= 7:
            grid[x][y] = grid[x][y]+val
        else:
            continue    
    # upper right
    for i in range(1,7):
        x = row + i
        y = col + i
        if x <= 7 and y <= 7:
            grid[x][y] = grid[x][y]+val
        else:
            continue 
    if val != 1:
        grid[row][col] = 0
    return grid


# In[3]:


def gprint(grid):
    for i in range(8):
        for j in range(8):
            if grid[i][j] == 99:
                print("Q   ",end='')
            elif grid[i][j] == 0:
                print(".   ",end='')
            else:
                print("x   ",end='')
        print('\n')
    print('\n')


# In[4]:


def possible(row,col,grid):
    if grid[row][col] == 0:
        return True
    else:
        return False


# In[5]:


grid = [[0 for i in range(8)] for j in range(8)]
count = 0

def solve(row):
    global grid
    global count
    if row == 8:
        count = count + 1
        print(count)
        gprint(grid)
        return
    
    for col in range(8):
        if possible(row,col,grid):
            place(row,col,grid,1)
            solve(row+1)
            place(row,col,grid,-1)


# In[6]:


solve(0)

