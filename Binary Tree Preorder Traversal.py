from TreeNode import *
from typing import *
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

s = Solution()
h = createTree([1,'null',2,3])
print(s.preorderTraversal(h))