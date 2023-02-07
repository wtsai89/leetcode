from TreeNode import *
from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [root]
        depth = 0
        while q:
            qsize = len(q)
            while qsize:
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                qsize -= 1
            depth += 1

        return depth

s = Solution()
a = [3,9,20,'null','null',15,7]
root = createTree(a)
print(s.maxDepth(root))
print(listify(root))