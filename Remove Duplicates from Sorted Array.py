from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        k = 1

        for i in range(len(nums)):
            if nums[p1] != nums[i]:
                k += 1
                p1 += 1
                nums[p1] = nums[i]

        return k

s = Solution()

a = [1,1,2]
print(s.removeDuplicates(a))
print(a)
