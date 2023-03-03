from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combo(arr, sum, nums):
            for i in range(len(nums)):
               newSum = sum + nums[i]
               if newSum == target:
                   ans.append(arr + [nums[i]])
               elif newSum < target:
                   combo(arr + [nums[i]], newSum, nums[i:])

        ans = []
        combo([], 0, candidates)
        return ans
    
s = Solution()
print(s.combinationSum([2,3,6,7],7))