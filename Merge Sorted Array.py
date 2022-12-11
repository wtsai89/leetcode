from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - 1
        m -= 1
        n -= 1
        while n >= 0:
            if m < 0 or nums2[n] > nums1[m]:
                nums1[i] = nums2[n]
                n -= 1
            else:
                nums1[i] = nums1[m]
                m -= 1
            i -= 1

s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
s.merge(nums1,3,nums2,3)
print(nums1)