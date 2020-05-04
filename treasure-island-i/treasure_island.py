import math
from collections import deque

def is_end(pos, m):
    return m[pos[0]][pos[1]] == 'X'

def get_conns(pos, m, closed):
    h = len(m)
    w = len(m[0])
    nxt = [(pos[0]-1, pos[1]), (pos[0]+1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1),]
    nxt = filter(lambda x: x[0] >= 0 and x[1] >= 0 and x[0] < h and x[1] < w, nxt)
    nxt = filter(lambda x: m[x[0]][x[1]] != 'D', nxt)
    nxt = filter(lambda x: not closed[x[0]][x[1]], nxt)
    return list(nxt)

def get_next(cost, closed):
    h = len(cost)
    w = len(cost[0])
    min_cost = math.inf
    for i in range(h):
        for j in range(w):
            if not closed[i][j] and cost[i][j] < min_cost:
                min_cost = cost[i][j]
                nxt = (i,j)
    return nxt

def is_start(pos):
    return pos[0] == 0 and pos[1] == 0

def path(pos, paths):
    path = []
    current = pos
    while not is_start(current):
        path.append(current)
        current = paths[current[0]][current[1]]
    path.append(current)
    path.reverse()
    return path

def treasure_path(m):
    h = len(m)
    w = len(m[0])
    path_from = [[None]*w for i in range(h)]
    path_cost = [[math.inf]*w for i in range(h)]
    path_closed = [[False]*w for i in range(h)]
    path_cost[0][0] = 0
    current = (0,0)
    while True:
        if is_end(current, m):
            return path(current, path_from)
        cost = path_cost[current[0]][current[1]]+1
        conns = get_conns(current, m, path_closed)
        for conn in conns:
            path_cost[conn[0]][conn[1]] = cost
            path_from[conn[0]][conn[1]] = current
        path_closed[current[0]][current[1]] = True
        current = get_next(path_cost, path_closed)
        