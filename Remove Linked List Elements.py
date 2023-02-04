from typing import Optional
from ListNode import *

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prehead = ListNode(0,head)
        curr = prehead
        while curr and curr.next:
            if curr.next.val == val:
                curr.next= curr.next.next
            else:
                curr = curr.next

        return prehead.next

s = Solution()
head = createLL([1,2,6,3,4,5,6])
ans = s.removeElements(head, 6)
print(listify(ans))