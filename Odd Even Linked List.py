from typing import Optional
from ListNode import *
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        if not odd or not odd.next:
            return odd
        even, ehead = odd.next, odd.next
        
        while even.next:
            odd.next = even.next
            odd = odd.next
            if not odd.next:
                even.next = None
                break
            even.next = odd.next
            even = even.next

        odd.next = ehead
        return head

s = Solution()
h = createLL([1,2,3,4,5])
h2 = s.oddEvenList(h)
print(listify(h2))