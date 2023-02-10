from typing import Optional
from TreeNode import *
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = [root]
        d = set()
        while q:
            qsize = len(q)
            while qsize:
                node = q.pop(0)
                if node.val in d:
                    return True
                d.add(k - node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                qsize -= 1

        return False
    
s = Solution()
r = createTree([5,3,6,2,4,'null',7])
print(s.findTarget(r,9))
