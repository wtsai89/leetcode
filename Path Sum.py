from typing import *
from TreeNode import *
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            if root.val == targetSum:
                return True
            else:
                return False
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

s = Solution()
h = createTree([5,4,8,11,'null',13,4,7,2,'null','null','null',1])
print(s.hasPathSum(h,22))