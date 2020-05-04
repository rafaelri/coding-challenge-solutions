def num_ways_paint(n, prev=None):
    if n == 1:
        if prev == 'y':
            return 1
        else: 
            return 2
    else:
        if prev == 'y':
            return num_ways_paint(n-1, 'g')
        else:
            return num_ways_paint(n-1, 'y')+num_ways_paint(n-1, 'g')
