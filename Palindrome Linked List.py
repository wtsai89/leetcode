from ListNode import *
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        def reverse(head):
            curr = head
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
    
        p1,p2 = head,head
        while p1:
            p1 = p1.next
            p2 = p2.next
            if p1:
                p1 = p1.next
        p1 = head
        p2 = reverse(p2)

        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True

s = Solution()
a = [1,2,2,1]
head = createLL(a)
print(s.isPalindrome(head))