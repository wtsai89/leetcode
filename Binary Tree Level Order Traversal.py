from TreeNode import *
from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            qsize = len(q)
            row = []
            while qsize:
                node = q.pop(0)
                row.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                qsize -= 1
            ans.append(row)

        return ans

s = Solution()
root = createTree([3,9,20,'null','null',15,7])
print(s.levelOrder(root))