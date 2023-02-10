from typing import Optional
from TreeNode import *
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        curr = root
        while curr:
            prev = curr
            if val > curr.val:
                curr = curr.right
                direction = 1
            else:
                curr = curr.left
                direction = 0

        if direction:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
        
        return root

s = Solution()
r = createTree([4,2,7,1,3])
r = s.insertIntoBST(r, 5)
print(listify(r))