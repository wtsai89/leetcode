from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        end = 0
        try:
            while(strs == [strs[i] for i in range(len(strs)) if strs[0][end] == strs[i][end]]):
                end += 1
        except:
            pass
        
        return strs[0][:end]

s = Solution()
strs = ["flower","flow","flight"]
print(s.longestCommonPrefix(strs))