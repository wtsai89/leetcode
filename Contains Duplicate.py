from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

s = Solution()
a = [1,2,3,1]
print(s.containsDuplicate(a))