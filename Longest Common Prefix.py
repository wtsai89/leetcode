from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        try:
            idx = 0
            while idx < len(strs[0]):
                for s in strs[1:]:
                    if s[idx] != strs[0][idx]:
                        return strs[0][:idx]
                idx += 1
        except:
           pass
        return strs[0][:idx]
s = Solution()
strs = ["flower","flow","flight"]
print(s.longestCommonPrefix(strs))