from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(lambda:0)
        for i in words:
            d[i] += 1

        kv = [(i,d[i]) for i in d]
        kv.sort(key=lambda x: (-x[1],x[0]))
        ans = []
        for i in range(k):
            ans.append(kv[i][0])

        return ans

s = Solution()
print(s.topKFrequent(["i","love","leetcode","i","love","coding"],2))