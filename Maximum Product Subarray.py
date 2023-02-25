from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans, ps = nums[0], {nums[0]}

        for i in nums[1:]:
            ps = [i*p for p in ps] + [i]
            maxp, minp = max(ps), min(ps)
            ans = max(ans, maxp)
            ps = {maxp, minp}

        return ans


s = Solution()
print(s.maxProduct([2,3,-2,4]))