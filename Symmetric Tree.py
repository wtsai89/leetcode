from TreeNode import *
from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = [root.left, root.right]
        while q:
            right = []
            length = len(q)
            for _ in range(length//2):
                rnode = q.pop(length-1)
                lnode = q.pop(0)
                length -= 2
                if lnode and rnode:
                    if lnode.val != rnode.val:
                        return False
                    q.append(lnode.left)
                    q.append(lnode.right)
                    right.append(rnode.right)
                    right.append(rnode.left)
                elif lnode or rnode:
                    return False
            q += right[::-1]

        return True

s = Solution()
root = createTree([1,2,2,3,4,4,3])
print(s.isSymmetric(root))