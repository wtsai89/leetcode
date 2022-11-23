class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m-n+1):
            nind = 0
            hind = i
            while nind < n and haystack[hind] == needle[nind]:
                nind += 1
                hind += 1
            if nind == n:
                return i
                
        return -1

s = Solution()
h = "sadbutsad"
n = "sad"
print(s.strStr(h,n))