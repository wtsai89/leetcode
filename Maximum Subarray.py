import sys

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, s = -sys.maxsize-1, -sys.maxsize-1
        for i in nums:
            if i > s + i:
                s = i
            else:
                s += i
            if s > ans:
                ans = s

        return ans

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))