from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1

s = Solution()
print(s.firstUniqChar("leetcode"))