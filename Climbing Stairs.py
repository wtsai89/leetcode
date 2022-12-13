class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev, pprev = 2, 1
        c = 2
        while c < n:
            temp = prev
            prev += pprev
            pprev = temp
            c += 1
        
        return prev

s = Solution()
print(s.climbStairs(4))