def get_starts(boggle, letter):
    h = len(boggle)
    w = len(boggle[0])
    res = []
    for i in range(0,h):
        for j in range(0,w):
            if boggle[i][j] == letter:
                res.append((i,j))
    return res 

def get_next(boggle, visited, pos, letter):
    h = len(boggle)
    w = len(boggle[0])
    x = pos[0]
    y = pos[1]
    res = [ (x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1,y+1), (x-1,y+1),(x+1,y-1), (x-1,y-1) ]
    res = filter(lambda z: z[0] >=0 and z[0] < h and z[1] >= 0 and z[1] < w, res)
    res = filter(lambda z: boggle[z[0]][z[1]] == letter, res)
    res = filter(lambda z: visited[z[0]][z[1]] == 0, res)
    return list(res) 

def is_word(boggle, word, visited=None, pos=None):
    if not word:
        return True

    if not visited:
        h = len(boggle)
        w = len(boggle[0])
        visited = [ [0]*w for i in range(h) ]

        for start in get_starts(boggle, word[0]):
            visited[start[0]][start[1]]=1
            return is_word(boggle, word[1:], visited, start)
            visited[start[0]][start[1]]=0
        else:
            return False
    else:
        for nxt in get_next(boggle, visited, pos, word[0]):
            visited[nxt[0]][nxt[1]]=1
            return is_word(boggle, word[1:], visited, nxt)
            visited[nxt[0]][nxt[1]]=0
        else:
            return False


