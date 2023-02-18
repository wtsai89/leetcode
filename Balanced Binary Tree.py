from typing import Optional
from TreeNode import *

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right) + 1

        return depth(root) != -1

s = Solution()
r = createTree([3,9,20,'null','null',15,7])
print(s.isBalanced(r))