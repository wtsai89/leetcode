class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss , st = [], []
        for c in s:
            if c == "#":
                if ss:
                    ss.pop()
            else:
                ss.append(c)

        for c in t:
            if c == "#":
                if st:
                    st.pop()
            else:
                st.append(c)
        
        return ss == st

s = Solution()
print(s.backspaceCompare("ab#c","ad#c"))