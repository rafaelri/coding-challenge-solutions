def humanDays(matrix):
    zombies = get_rows(matrix, 1)
    if not zombies:
        return -1
    ctr = 0
    humans = get_rows(matrix, 0)
    while humans:
        infect(matrix, zombies)
        humans = get_rows(matrix, 0)
        zombies = get_rows(matrix, 1)
        ctr+=1
    return ctr

def infect(matrix, zombies):
    h = len(matrix)
    w = len(matrix[0])
    for zombie in zombies:
        for adjacent in adjacents(zombie, h, w):
            matrix[adjacent[0]][adjacent[1]] = 1

def adjacents(zombie, h, w):
    x = zombie[0]
    y = zombie[1]
    res = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    def valid(pos):
        return pos[0] >= 0 and pos[0] < h and pos[1] >= 0 and pos[1] < w
    return list(filter(valid, res))

def get_rows(matrix, val):
    h = len(matrix)
    w = len(matrix[0])
    res = []
    for i in range(0,h):
        for j in range(0,w):
            if matrix[i][j] == val:
                res.append((i,j))
    return res