from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        p,pp,ppp = 0,0,0
        for i in nums:
            p,pp,ppp = i + max(pp,ppp), p, pp
        
        return max(p,pp)

s = Solution()
print(s.rob([2,7,9,3,1]))