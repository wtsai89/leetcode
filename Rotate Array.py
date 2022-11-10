from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reversal(start, end):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1
        
        k = k % len(nums)
        if k > 0:
            reversal(0, len(nums)-1)
            reversal(0, k-1)
            reversal(k, len(nums)-1)

s = Solution()
a = [1,2,3,4,5,6,7]
s.rotate(a,3)
print(a)