from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cMin = pow(10,4)+1
        profit = 0
        for i in prices:
            if i < cMin:
                cMin = i
            elif i - cMin > profit:
                profit = i - cMin
                
        return profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))