class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        values = set()

        for i in range(len(s)):
            sc = s[i]
            tc = t[i]

            if sc not in d:
                if tc in values:
                    return False
                d[sc] = tc
                values.add(tc)
            elif d[sc] != tc:
                return False

        return True

s = Solution()
print(s.isIsomorphic("egg","add"))