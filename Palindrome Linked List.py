from ListNode import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #find mid
        p1, p2 = head, head
        
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        
        #reverse second half
        curr = p1.next
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #compare 1st and 2nd half
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True

s = Solution()
a = [1,2,2,1]
head = createLL(a)
print(s.isPalindrome(head))