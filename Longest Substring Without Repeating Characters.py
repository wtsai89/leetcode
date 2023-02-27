class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dups = set()
        start, ans = 0, 0

        for i, c in enumerate(s):
            while c in dups:
                dups.remove(s[start])
                start += 1
            dups.add(c)
            ans = max(ans, i-start+1)

        return ans
    
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))