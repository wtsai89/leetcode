from typing import Optional
from TreeNode import *

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.k -= 1
            if not self.k:
                self.res = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.res
    
s = Solution()
r = createTree([3,1,4,'null',2])
print(s.kthSmallest(r,1))