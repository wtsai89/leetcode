class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        while n != 1:
            sum = 0
            while n > 0:
                sum += (n % 10) ** 2
                n = n // 10
            if sum in cycle:
                return False
            cycle.add(sum)
            n = sum

        return True

s = Solution()
print(s.isHappy(19))