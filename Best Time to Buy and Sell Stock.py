from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = pow(10,4)+1

        for sell in prices:
            if sell < buy:
                buy = sell
            else:
                if sell - buy > ans:
                    ans = sell - buy

        return ans

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))