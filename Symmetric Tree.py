from TreeNode import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root.left, root.right]
        while queue:
            qsize = len(queue)
            rQ = []
            while qsize:
                lnode = queue.pop(0)
                qsize -= 1
                if not qsize:
                    return False
                rnode = queue.pop(qsize-1)
                qsize -= 1
                
                if (lnode and not rnode) or (rnode and not lnode):
                    return False
                if lnode and rnode:
                    if lnode.val != rnode.val:
                        return False
                    queue.append(lnode.left)
                    queue.append(lnode.right)
                    rQ.insert(0, rnode.right)
                    rQ.insert(0, rnode.left)
            queue += rQ
            
        return True

s = Solution()
root = createTree([1,2,2,3,4,4,3])
print(s.isSymmetric(root))