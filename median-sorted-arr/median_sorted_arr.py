from typing import List
class Solution():
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        even = (n+m) % 2 == 0
        ctr = 0
        i = j = 0
        if even:
            end = ((n+m) // 2)-1
            while ctr < end:
                if j == m or (i < n and nums1[i] < nums2[j]):
                    i+=1
                else:
                    j+=1
                ctr+=1
            if j == m or (i < n and nums1[i] < nums2[j]):
                v1 = nums1[i]
                i+=1
            else:
                v1 = nums2[j]
                j+=1
            if j == m or (i < n and nums1[i] < nums2[j]):
                v2 = nums1[i]
                i+=1
            else:
                v2 = nums2[j]
                j+=1
            print(v1)
            print(v2)
            return (v1+v2)/2
        else:
            end = (n+m) // 2
            while ctr < end:
                if j == m or (i < n and nums1[i] < nums2[j]):
                    i+=1
                else:
                    j+=1
                ctr+=1
            if j == m or (i < n and nums1[i] < nums2[j]):
                return nums1[i]
            else:
                return nums2[j]