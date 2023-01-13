from typing import List
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = (left+right)//2
            if nums[mid] < 0:
                left = mid+1
            else:
                if mid == 0 or nums[mid-1] < 0:
                    left = mid
                    break
                right = mid-1
        negEnd = left
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = (left+right)//2
            if nums[mid] > 0:
                right = mid-1
            else:
                if nums[mid+1] > 0:
                    right = mid
                    break
                left = mid+1
        posStart = right
        
        return max(negEnd, len(nums)-1-posStart)

s = Solution()
print(s.maximumCount([-3,-2,-1,0,0,1,2]))