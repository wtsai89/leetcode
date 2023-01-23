from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        curr, prev = 0, 0
        for i in cost:
            temp = curr
            curr = i + min(prev, curr)
            prev = temp

        return min(prev, curr)

s = Solution()
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))