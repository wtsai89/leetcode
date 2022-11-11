from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans

s = Solution()
a = [4,1,2,1,2]
print(s.singleNumber(a))