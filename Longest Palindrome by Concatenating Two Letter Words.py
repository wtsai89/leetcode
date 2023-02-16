from collections import defaultdict
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        comp = defaultdict(lambda: 0)
        doubles = 0
        ans = 0

        for w in words:
            if w[0] == w[1]:
                if comp[w]:
                    ans += 4
                    comp[w] -= 1
                    doubles -= 1
                else:
                    comp[w] += 1
                    doubles += 1
            elif comp[w]:
                ans += 4
                comp[w] -= 1
            else:
                comp[w[::-1]] += 1

        if doubles:
            ans += 2

        return ans
    
s = Solution()
print(s.longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))