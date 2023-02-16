from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        maxreps = max(d.values())
        largesttaskscount = len([i for i in d if d[i] == maxreps])

        if largesttaskscount > n:
            return len(tasks)
        
        return max(largesttaskscount + (n+1) * (maxreps-1), len(tasks))
    
s = Solution()
print(s.leastInterval(["A","A","A","B","B","B"],2))