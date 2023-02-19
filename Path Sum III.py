from typing import Optional
from TreeNode import *

class Solution:
    def __init__(self):
        self.paths = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def path(node):
            if not node:
                return []
            sums = path(node.left) + path(node.right)
            sums = [node.val+i for i in sums] + [node.val]
            for i in sums:
                if i == targetSum:
                    self.paths += 1
            return sums

        path(root)
        return self.paths
    
s = Solution()
r = createTree([10,5,-3,3,2,'null',11,3,-2,'null',1])
print(s.pathSum(r,8))