from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = Counter(magazine)
        for i in ransomNote:
            if d[i]:
                d[i] -= 1
            else:
                return False

        return True

s = Solution()
print(s.canConstruct("aa","aab"))