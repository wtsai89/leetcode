from typing import Optional
from ListNode import *
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                p2 = curr.next.next
                while p2 and p2.val == curr.val:
                    p2 = p2.next
                curr.next = p2
            curr = curr.next

        return head

s = Solution()
head = createLL([1,1,2,3,3])
ans = s.deleteDuplicates(head)
print(listify(ans))