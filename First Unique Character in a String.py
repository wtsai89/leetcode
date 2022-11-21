from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for i in d:
            if d[i] == 1:
                return s.index(i)
        return -1

s = Solution()
print(s.firstUniqChar("leetcode"))