def nsp(x,y):
    '''
    Calcualte shortest path from bottom left to upper right in x by y grid
    nsp(x,y) - x is ending x-coordinate, y is ending y-coordinate
    assumes starting at (0,0)
    '''
    if x == 0 and y == 0:
        return 2
    elif y == 0 and x > 0:
        return 1
    elif y > 0 and x == 0:
        return 1
    else:
        return nsp(x-1,y) + nsp(x,y-1)


print(nsp(2,3))


