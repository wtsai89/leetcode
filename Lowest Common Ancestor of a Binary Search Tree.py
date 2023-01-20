from TreeNode import *
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = [root]
        while queue:
            node = queue.pop(0)
            if p.val < node.val and q.val < node.val:
                queue.append(node.left)
            if p.val > node.val and q.val > node.val:
                queue.append(node.right)
        return node

s = Solution()
r = createTree([6,2,8,0,4,7,9,'null','null',3,5])
ans = s.lowestCommonAncestor(r,r.left,r.left.right)
print(listify(ans))