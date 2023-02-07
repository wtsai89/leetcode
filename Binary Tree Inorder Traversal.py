from TreeNode import *
from typing import *

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val]  + self.inorderTraversal(root.right)

s = Solution()
h = createTree([1,'null',2,3])
print(s.inorderTraversal(h))