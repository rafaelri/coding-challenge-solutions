def maxPathScore(matrix):
    start = (0,0)
    h = len(matrix)
    w = len(matrix[0])
    return max_of_min(matrix, start, h, w, matrix[0][0])

def get_next(matrix, pos, h, w):
    moves = [(pos[0], pos[1]+1), (pos[0]+1, pos[1])]
    return list(filter( lambda xy: xy[0]<h and xy[1]<w, moves ))

def max_of_min(matrix, position, h, w, min_value):
    next_pos = get_next(matrix, position, h, w)
    if not next_pos:
        return min_value
    else:
        def next_min(pos):
            val_pos = matrix[pos[0]][pos[1]]
            new_min = val_pos if val_pos < min_value else min_value
            return max_of_min(matrix, pos, h, w, new_min)
        minuses = map(next_min, next_pos)
        return max(minuses)
