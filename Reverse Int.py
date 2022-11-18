import math

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        maxInt = pow(2,31)-1
        minInt = -pow(2,31)
        
        while x != 0:
            if x > 0:
                pop = x % 10
                if rev > maxInt//10 or (rev == maxInt//10 and pop > 7):
                    return 0
                x = x // 10
            else:
                pop = x % -10
                if rev < math.ceil(minInt/10) or (rev == minInt//10 and pop < -8):
                    return 0
                x = math.ceil(x / 10)
            
            rev = rev * 10 + pop
            
        return rev

s = Solution()
print(s.reverse(-123))