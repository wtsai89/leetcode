from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = Counter(nums1)
        a = []
        
        for i in nums2:
            if d[i]:
                a.append(i)
                d[i] -= 1
                
        return a

n1 = [4,9,5]
n2 = [9,4,9,8,4]

s = Solution()
print(s.intersect(n1,n2))