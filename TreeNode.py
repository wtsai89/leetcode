class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(arr):
    root = TreeNode(arr.pop(0))
    queue = [root]
    while arr:
        node = queue.pop(0)
        val = arr.pop(0)
        if val != 'null':
            node.left = TreeNode(val)
            queue.append(node.left)
        if arr:
            val = arr.pop(0)
            if val != 'null':
                node.right = TreeNode(val)
                queue.append(node.right)
    
    return root

def listify(root):
    queue = [root]
    a = []
    while queue:
        qsize = len(queue)
        while qsize:
            node = queue.pop(0)
            if node:
                a.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                a.append('null')
            qsize -= 1

    for i in range(len(a)-1,-1,-1):
        if a[i] == 'null':
            a.pop()
        else:
            break

    return a