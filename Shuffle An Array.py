from random import randint
from typing import List
class Solution:

    def __init__(self, nums: List[int]):
        self.og = nums.copy()

    def reset(self) -> List[int]:
        return self.og.copy()

    def shuffle(self) -> List[int]:
        nums = self.og.copy()
        for i in range(len(nums)):
            j = randint(0,len(nums)-1)
            nums[i], nums[j] = nums[j], nums[i]
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

s = Solution([1,2,3])
s1 = s.shuffle()
s2 = s.reset()
s3 = s.shuffle()
print(f"{s},{s1},{s2},{s3}")