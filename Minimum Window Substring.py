from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        toMatch = set()
        tmap = defaultdict(lambda: 0)
        for c in t:
            tmap[c] += 1
            toMatch.add(c)
        smap = defaultdict(lambda: 0)
        mcc = 0 #matching char count
        left = 0

        while left < len(s) and s[left] not in toMatch:
            left += 1
        right = left
        while mcc != len(toMatch) and right < len(s):
            c = s[right]
            if c in toMatch:
                smap[c] += 1
                if smap[c] == tmap[c]:
                    mcc += 1
            right += 1
        if mcc != len(toMatch):
            return ""
        
        while s[left] not in toMatch or smap[s[left]] > tmap[s[left]]:
            smap[s[left]] -= 1
            left += 1       
        ans = s[left:right]
        while right < len(s):
            c = s[right]
            if c in toMatch:
                smap[c] += 1
                while s[left] not in toMatch or smap[s[left]] > tmap[s[left]]:
                    smap[s[left]] -= 1
                    left += 1
                if right-left+1 < len(ans):
                    ans = s[left:right+1]
            right += 1

        return ans
    
s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))