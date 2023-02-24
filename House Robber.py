from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        curr, prev, pprev = 0, 0, 0
        for i in nums:
            temp = curr
            curr = i + max(prev, pprev)
            pprev = prev
            prev = temp
        return max(curr, prev)

s = Solution()
print(s.rob([2,7,9,3,1]))