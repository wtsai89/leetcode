from typing import Optional
from TreeNode import *

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return [0,0]
            left, a1 = depth(node.left)
            right, a2 = depth(node.right)
            ans = max(a1, a2, left + right)
            return [max(left, right) + 1, ans]

        return depth(root)[1]

s = Solution()    
r = createTree([1,2,3,4,5])
print(s.diameterOfBinaryTree(r))