from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False

s = Solution()
a = [1,2,3,1]
print(s.containsDuplicate(a))