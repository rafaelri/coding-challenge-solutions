from collections import deque
def get_unvisited(mat):
    h = len(mat)
    w = len(mat[0])
    unvisited = set()
    for i in range(h):
        for j in range(w):
            unvisited.add((i,j))
    return unvisited

def get_next(pos, mat, unvisited):
    h = len(mat)
    w = len(mat[0])
    nxt = [(pos[0]-1, pos[1]), (pos[0]+1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1)]
    nxt = filter(lambda x: x[0] >=0 and x[1] >=0 and x[0] < h and x[1] < w, nxt)
    nxt = filter(lambda x: x in unvisited, nxt)
    nxt = filter(lambda x: mat[pos[0]][pos[1]] == mat[x[0]][x[1]], nxt)
    return list(nxt)

def count_countries(mat):
    unvisited = get_unvisited(mat)
    q = deque()
    ctr = 0
    while unvisited:
        if not q:
            ctr = ctr+1
            current = unvisited.pop()
            print('from unvisited ' + str(current))
        else:
            current = q.popleft()
            print('from next ' + str(current))
        for i in get_next(current, mat, unvisited):
            print('next ' + str(i))
            q.append(i)
            unvisited.remove(i)
        
    return ctr