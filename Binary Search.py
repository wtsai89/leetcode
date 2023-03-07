from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums) - 1

        while first < last:
            mid = (first + last) // 2
            if target < nums[mid]:
                last = mid - 1
            elif target > nums[mid]:
                first = mid + 1
            else:
                return mid
        
        if nums[first] != target:
            return -1
        return first

s = Solution()
print(s.search([-1,0,3,5,9,12],9))