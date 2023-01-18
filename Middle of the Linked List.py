from ListNode import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if not fast:
                return slow
            fast = fast.next
        return slow

s = Solution()
h = createLL([1,2,3,4,5])
ans = s.middleNode(h)
print(listify(ans))