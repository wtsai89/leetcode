from typing import Optional
from TreeNode import *
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == val:
            return root
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

s = Solution()
r = createTree([4,2,7,1,3])
r2 = s.searchBST(r,2)
print(listify(r2))