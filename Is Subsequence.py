class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        subi = 0
        for c in t:
            if s[subi] == c:
                subi += 1
                if subi == len(s):
                    return True
        
        return False
        
s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))