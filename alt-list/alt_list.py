from collections import deque
def reorder_alt_list(l):
    res = []
    i = 0
    j = len(l)-1
    while i<=j:
        res.append(l[i])
        res.append(l[j])
        i+=1
        j-=1
    if len(l) % 2 == 1:
        res.pop()
    return res