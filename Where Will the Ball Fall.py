from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        width = len(grid[0])
        height = len(grid)
        for i in range(width):
            r, c, broke = 0, i, False
            for j in range(height):
                if grid[r][c] == 1:
                    if c == width-1 or grid[r][c+1] == -1:
                        broke = True
                        break
                    c += 1
                else:
                    if c == 0 or grid[r][c-1] == 1:
                        broke = True
                        break
                    c -= 1
                r += 1
            if broke:
                ans.append(-1)
            else:
                ans.append(c)

        return ans

s = Solution()
print(s.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))