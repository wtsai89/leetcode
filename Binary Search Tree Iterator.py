from typing import Optional
from TreeNode import *

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iter = root
        self.stack = []
        while self.iter:
            self.stack.append(self.iter)
            self.iter = self.iter.left

    def next(self) -> int:
        while self.iter:
            self.stack.append(self.iter)
            self.iter = self.iter.left
        if not self.iter:
            self.iter = self.stack.pop()
        val = self.iter.val
        self.iter = self.iter.right
        return val

    def hasNext(self) -> bool:
        return self.iter or self.stack