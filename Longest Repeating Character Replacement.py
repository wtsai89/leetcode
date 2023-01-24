class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        d = {}

        for right in range(len(s)):
            length = right - left + 1
            addchar = s[right]
            d[addchar] = d.get(addchar, 0) + 1

            if length - max(d.values()) <= k:
                if length > ans:
                    ans = length
            else:
                d[s[left]] -= 1
                left += 1

        return ans

s = Solution()
print(s.characterReplacement("AABABBA",1))