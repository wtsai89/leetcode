from typing import Optional
from TreeNode import *
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = [root]
        while q:
            qsize = len(q)
            while qsize:
                node = q.pop(0)
                node.left, node.right = node.right, node.left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                qsize -= 1

        return root

s = Solution()
h = createTree([4,2,7,1,3,6,9])
h = s.invertTree(h)
print(listify(h))