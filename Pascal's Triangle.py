from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows-1):
            prev = ans[i]
            row = [1]
            for j in range(len(prev)-1):
                row.append(prev[j]+prev[j+1])
            row.append(1)
            ans.append(row)
        return ans

s = Solution()
print(s.generate(5))