from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nz = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nz], nums[i] = nums[i], nums[nz]
                nz += 1

s= Solution()
a = [0,1,0,3,12]
s.moveZeroes(a)
print(a)