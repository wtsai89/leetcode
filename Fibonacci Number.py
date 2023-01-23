class Solution:
    def fib(self, n: int) -> int:
        f = [0,1]
        if n <= 1:
            return f[n]
        for i in range(2,n+1):
            f.append(f[i-1]+f[i-2])
        return f[n]

s = Solution()
print(s.fib(4))