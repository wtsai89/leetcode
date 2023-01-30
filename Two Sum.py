from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            val = nums[i]
            if val in d:
                return [i, d[val]]
            d[target-val] = i

        return []

s = Solution()
a = [2,7,11,15]
print(s.twoSum(a,9))