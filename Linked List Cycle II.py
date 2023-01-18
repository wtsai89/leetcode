from ListNode import *
from typing import Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None

        while head != slow:
            head = head.next
            slow = slow.next

        return head

s = Solution()
h = createLL([3,2,0,-4])
loopStart = index(h,1)
loopEnd = index(h,3)
loopEnd.next = loopStart
ans = s.detectCycle(h)
print(listify(ans,loopEnd))