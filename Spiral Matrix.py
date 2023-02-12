from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c, horiz, vert = 0, -1, len(matrix[0]), len(matrix)-1
        ans = []
        direction = 1
        while horiz: 
            for _ in range(horiz):
                c += direction
                ans.append(matrix[r][c])
            if not vert:
                break
            for _ in range(vert):
                r += direction
                ans.append(matrix[r][c])      
            horiz -= 1
            vert -= 1
            direction *= -1
        return ans
s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))