from TreeNode import *
from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        a = []
        while queue:
            qsize = len(queue)
            aa = []
            while qsize:
                node = queue.pop(0)
                aa.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                qsize -= 1
            a += [aa]
        return a

s = Solution()
root = createTree([3,9,20,'null','null',15,7])
print(s.levelOrder(root))