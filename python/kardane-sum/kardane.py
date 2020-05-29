from typing import List

def largest_sum(ints: List[int]) -> int:
    if not ints:
        return 0
    lg = ints[0]
    curr = lg
    for i in range(1, len(ints)):
        added = curr + ints[i]
        if added > curr:
            curr = added
            if curr > lg:
                lg = curr
        else:
            curr = ints[i]
    return lg
    
print(largest_sum([3, 3, -4, 3, 2]))