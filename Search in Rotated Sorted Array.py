from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[mid] or target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1

        if nums[left] == target:
            return left
        return -1
    
s = Solution()
print(s.search([4,5,6,7,8,1,2,3],8))