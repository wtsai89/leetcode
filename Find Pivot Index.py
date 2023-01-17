from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = 0
        for i in nums:
            right += i
        
        for i in range(len(nums)):
            n = nums[i]
            right -= n
            if left == right:
                return i
            left += n

        return -1

s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))