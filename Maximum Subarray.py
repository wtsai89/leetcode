from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cSum = 0
        sol = -pow(10,4)-1
        
        for i in nums:
            cSum = max(i,cSum+i)
            sol = max(sol,cSum)
        
        return sol

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))