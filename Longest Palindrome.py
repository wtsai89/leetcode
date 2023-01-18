from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)

        single = 0
        for k in d:
            if d[k] % 2 == 1:
                single = 1
                break
        
        ans = 0
        for k in d:
            ans += d[k] - (d[k]%2)

        return ans + single

s = Solution()
print(s.longestPalindrome("abccccdd"))