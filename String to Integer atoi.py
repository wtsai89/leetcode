import math
class Solution:
    def myAtoi(self, s: str) -> int:
        a = 0
        sign = 1
        index = 0
        s = s.strip()
        for i in range(len(s)):
            c = s[i]
            if c == "-":
                sign = -1
                index = i+1
                break
            elif c == "+":
                index = i+1
                break
            elif c.isdigit():
                index = i
                break
            else:
                return 0
        
        for i in range(index, len(s)):
            if s[i].isdigit():
                a = a*10 + int(s[i])
            else:
                break
        
        a *= sign
        if a > math.pow(2,31) - 1:
            a = int(math.pow(2,31) - 1)
        if a < -math.pow(2,31):
            a = int(-math.pow(2,31))
        return a

s = "   -42"
sol = Solution()
print(sol.myAtoi(s))