from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1
        s = (int)((n/2)*(n-1))
        for i in nums:
            s -= i
        return s

s = Solution()
print(s.missingNumber([0,1]))