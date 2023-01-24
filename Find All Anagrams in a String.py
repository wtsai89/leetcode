from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(p) > len(s):
            return ans
        
        alpha = "abcdefghijklmnopqrstuvwxyz"
        pd = {c:0 for c in alpha}
        sd = {c:0 for c in alpha}

        for c in p:
            pd[c] += 1
        for i in range(len(p)):
            sd[s[i]] += 1
        score = 0
        for k in pd:
            if pd[k] == sd[k]:   
                score += 1
        if score == 26:
            ans.append(0)

        for i in range(1,len(s)-len(p)+1):
            deletechar = s[i-1]
            addchar = s[i+len(p)-1]
            if pd[deletechar] == sd[deletechar]:
                score -= 1
            if pd[addchar] == sd[addchar]:
                score -= 1 
            sd[deletechar] -= 1
            sd[addchar] += 1
            if pd[deletechar] == sd[deletechar]:
                score += 1
            if pd[addchar] == sd[addchar]:
                score += 1 
            
            if score == 26:
                ans.append(i)
        
        return ans

s = Solution()
print(s.findAnagrams("cbaebabacd","abc"))