from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2
        
        items = len(nums)
        knap = [True] + [False] * (target)

        for i in range(1,items+1):
            for w in range(target, 0, -1):
                knap[w] = knap[w] or (w-nums[i-1] >= 0 and knap[w-nums[i-1]])
        
        return knap[target]
    
s = Solution()
print(s.canPartition([1,2,5]))