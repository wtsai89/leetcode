from ListNode import *

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val = node.next.val
        
        while(node.next.next):
            node.next.val = node.next.next.val
            node = node.next
            
        node.next = None

arr = [4,5,1,9]
head = createLL(arr)
node = head

node = node.next
s = Solution()
s.deleteNode(node)

print(listify(head))