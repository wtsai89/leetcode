from TreeNode import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        queue = [(root,-pow(2,31)-1,pow(2,31))]
        while queue:
            qsize = len(queue)
            while qsize:
                node, lt, gt = queue.pop(0)
                if lt >= node.val:
                        return False
                if gt <= node.val:
                        return False
                if node.left:
                    queue.append((node.left,lt,node.val))
                if node.right:
                    queue.append((node.right,node.val,gt))
                qsize -= 1
        
        return True

s = Solution()
root = createTree([5,4,6,'null','null',3,7])
print(s.isValidBST(root))