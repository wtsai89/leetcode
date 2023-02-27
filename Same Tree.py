from typing import Optional
from TreeNode import *
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False       
        pq, qq = [p], [q]
        while pq:
            for _ in range(len(pq)):
                pnode = pq.pop(0)
                qnode = qq.pop(0)
                if pnode.val != qnode.val:
                    return False
                if pnode.left and qnode.left:
                    pq.append(pnode.left)
                    qq.append(qnode.left)
                elif pnode.left or qnode.left:
                    return False
                if pnode.right and qnode.right:
                    pq.append(pnode.right)
                    qq.append(qnode.right)
                elif pnode.right or qnode.right:
                    return False
        return True
    
s = Solution()
p = createTree([1,2])
q = createTree([1,'null',2])
print(s.isSameTree(p,q))