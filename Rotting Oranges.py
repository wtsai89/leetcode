from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        mins = 0
        while q:
            qsize = len(q)
            while qsize:
                r,c = q.pop(0)
                if r > 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    q.append((r-1,c))
                    fresh -= 1
                if r < len(grid)-1 and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    q.append((r+1,c))
                    fresh -= 1
                if c > 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    q.append((r,c-1))
                    fresh -= 1
                if c < len(grid[0])-1 and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    q.append((r,c+1))
                    fresh -= 1 
                qsize -= 1
            if q:
                mins += 1
        
        if fresh:
            return -1
        return mins


s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))