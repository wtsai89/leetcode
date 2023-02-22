from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        MOVE = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(r, c, valid):
            valid.add((r,c))
            for dy, dx in MOVE:
                y = r + dy
                x = c + dx
                if 0 <= y < m and 0 <= x < n and (y,x) not in valid and heights[r][c] <= heights[y][x]:
                    dfs(y, x, valid)
        m = len(heights)
        n = len(heights[0])

        pac_valid = set()
        at_valid = set()
        for i in range(m):
            dfs(i, 0, pac_valid)
            dfs(i, n-1, at_valid)
        for i in range(n):
            dfs(0, i, pac_valid)
            dfs(m-1, i, at_valid)

        return pac_valid & at_valid
    
s = Solution()
print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))