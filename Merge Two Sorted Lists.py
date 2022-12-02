from ListNode import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        prehead = ListNode()
        curr = prehead
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
            
        return prehead.next

s = Solution()
a1 = [1,2,4]
a2 = [1,3,4]
h1 = createLL(a1)
h2 = createLL(a2)

ans = s.mergeTwoLists(h1,h2)
print(listify(ans))