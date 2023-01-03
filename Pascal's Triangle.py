from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        s = [[1]]
        if numRows == 1:
            return s
        for i in range(numRows-1):
            row = [1]
            for j in range(len(s[i])-1):
                row.append(s[i][j]+s[i][j+1])
            row.append(1)
            s.append(row)
        return s

s = Solution()
print(s.generate(5))