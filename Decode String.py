class Solution:
    def decodeString(self, s: str) -> str:
        head = ""
        for i in range(len(s)):
            c = s[i]
            if c.isalpha():
                head = head + c
            elif c.isdigit():
                j = i
                while s[j].isdigit():
                    j += 1
                mult = int(s[i:j])
                bstack = 1
                k = j + 1
                while bstack > 0:
                    if s[k] == "[":
                        bstack += 1
                    elif s[k] == "]":
                        bstack -= 1
                    k += 1
                ss = s[j+1:k-1]
                tail = s[k:]
                return head + mult * self.decodeString(ss) + self.decodeString(tail)
        return head

s = Solution()
print(s.decodeString("3[a]2[bc]"))