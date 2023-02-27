from typing import Optional, List
from TreeNode import *

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        q = [root]
        while q:
            ans.append(q[-1].val)
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ans

s = Solution()
r = createTree([1,2,3,'null',5,'null',4])
print(s.rightSideView(r))