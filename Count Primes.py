from math import *
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        nums = [True for i in range(n)]
        ans = 0
        sqrt = int(ceil(pow(n,0.5)))
        for i in range(3,sqrt,2):
            if nums[i]:
                for j in range(int(pow(i,2)),n,i):
                    nums[j] = False
                ans += 1
        if sqrt % 2 == 0:
            sqrt += 1
        for i in range(sqrt,n,2):
            if nums[i]:
                ans += 1

        return ans + 1

s = Solution()
print(s.countPrimes(10))