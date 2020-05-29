from typing import List
from collections import deque
class Solution2():
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        s = set()
        nums.append(0)
        for i in range(0,l):
            if nums[i] < 0 or nums[i] > l:
                nums[i] = 0
            elif nums[i] == i:
                continue
            else:
                n = nums[i]
                if nums[n] != 0 and nums[n] <= l:
                    s.add(nums[n])
                nums[n] = n
                nums[i] = 0
            if s:
                rems = []
                for d in s:
                    if nums[d] == 0 or nums[d] == d:
                        rems.append(d)
                        nums[d] = d
                for r in rems:
                    s.remove(r)
        while s:
            rems = []
            for d in s:
                if nums[d] == 0 or nums[d] == d:
                    nums[d] = d
                    rems.append(d)
            for r in rems:
                s.remove(r)
                    
        for i in range(1,len(nums)):
            if nums[i] != i:
                return i
        return l+1
                        
#Solution().firstMissingPositive([10,4,16,54,17,-7,21,15,25,31,61,1,6,12,21,46,16,56,54,12,23,20,38,63,2,27,35,11,13,47,13,11,61,39,0,14,42,8,16,54,50,12,-10,43,11,-1,24,38,-10,13,60,0,44,11,50,33,48,20,31,-4,2,54,-6,51,6])                        

class Solution():
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        accum = (l+1) * [0]
        for i in range(0,l):
            if nums[i] > 0 and nums[i] <= l:
                accum[nums[i]] = nums[i]
        for i in range(1,len(accum)):
            if accum[i] != i:
                return i
        return l+1

Solution().firstMissingPositive([1,1000])