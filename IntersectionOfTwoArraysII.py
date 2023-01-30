from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)

        ans = []
        for i in d1:
            if i in d2:
                freq = min(d1[i],d2[i])
                for _ in range(freq):
                    ans.append(i)

        return ans

n1 = [4,9,5]
n2 = [9,4,9,8,4]

s = Solution()
print(s.intersect(n1,n2))