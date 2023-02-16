from typing import Optional
from ListNode import *
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(p1, p2, p1_size, p2_size):
            prehead = ListNode()
            curr = prehead
            while p1_size and p2_size:
                if p1.val <= p2.val:
                    curr.next = p1
                    curr = curr.next
                    p1 = p1.next
                    p1_size -= 1
                else:
                    curr.next = p2
                    curr = curr.next
                    p2 = p2.next
                    p2_size -= 1
            if not p2_size:
                curr.next = p1
            if not p1_size:
                curr.next = p2
            return prehead.next


        def mergeSort(head, size):
            if size <= 1:
                return head
            p2 = head
            mid = size // 2
            for _ in range(mid):
                p2 = p2.next
            p1 = mergeSort(head, mid)
            p2 = mergeSort(p2, size - mid)
            return merge(p1, p2, mid, size - mid)

        size = 0
        i = head
        while i:
            i = i.next
            size += 1
        head = mergeSort(head, size)
        
        i = head
        if size:
            for _ in range(size-1):
                i = i.next
            i.next = None
        return head
    
s = Solution()
h = createLL([4,2,1,3])
h = s.sortList(h)
print(listify(h))