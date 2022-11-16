from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [i, d[nums[i]]]
            else:
                d[target-nums[i]] = i

s = Solution()
a = [2,7,11,15]
print(s.twoSum(a,9))