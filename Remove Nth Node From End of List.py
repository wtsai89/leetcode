from ListNode import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prehead = ListNode(0, head)
        p1, p2 = prehead, prehead
        for i in range(n):
            p2 = p2.next
        
        while p2.next:
            p1 = p1.next
            p2 = p2.next
            
        p1.next = p1.next.next
        return prehead.next

arr = [1,2,3,4,5]
head = createLL(arr)

s = Solution()
head = s.removeNthFromEnd(head, 2)
print(listify(head))