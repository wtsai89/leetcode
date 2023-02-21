from TreeNode import *
from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(left, right):
            if left == right:
                return TreeNode(nums[left])
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            if right - left > 1:
                node.left = bst(left, mid-1)
            node.right = bst(mid+1, right)
            return node

        return bst(0, len(nums)-1)

s = Solution()
a = [-10,-3,0,5,9]
root = s.sortedArrayToBST(a)
print(listify(root))