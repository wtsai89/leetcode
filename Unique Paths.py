class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for i in range(m):
            row = []
            for j in range(n):
                if i == 0 or j == 0:
                    row.append(1)
                else:
                    row.append(row[j-1]+ grid[i-1][j])
            grid.append(row)
        return grid[m-1][n-1]

s = Solution()
print(s.uniquePaths(3,7))