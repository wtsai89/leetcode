from TreeNode import *
from typing import *

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

s = Solution()
h = createTree([1,'null',2,3])
print(s.postorderTraversal(h))