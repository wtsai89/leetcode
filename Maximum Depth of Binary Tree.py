from TreeNode import *
class Solution:         
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node, d):
            if node:
                return max(dfs(node.left,d+1),dfs(node.right,d+1))
            return d
        return dfs(root,0)

s = Solution()
a = [3,9,20,'null','null',15,7]
root = createTree(a)
print(s.maxDepth(root))
print(listify(root))