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
            qsize = len(q)
            right = []
            while qsize:
                lnode = q.pop(0)
                rnode = q.pop(qsize-2)
                try:
                    if not lnode and not rnode:
                        pass
                    elif lnode.val == rnode.val:
                        q.append(lnode.left)
                        q.append(lnode.right)
                        right.insert(0,rnode.right)
                        right.insert(0,rnode.left)
                    else:
                        return False
                except:
                    return False
                qsize -= 2
            q += right

        return True

s = Solution()
root = createTree([1,2,2,3,4,4,3])
print(s.isSymmetric(root))