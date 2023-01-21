from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == color:
            return image
        q = [[sr,sc]]
        while q:
            r, c = q.pop(0)
            image[r][c] = color
            if r > 0 and image[r-1][c] == oldColor:
                q.append([r-1,c])
            if r < len(image)-1 and image[r+1][c] == oldColor:
                q.append([r+1,c])
            if c > 0 and image[r][c-1] == oldColor:
                q.append([r,c-1])
            if c < len(image[0])-1 and image[r][c+1] == oldColor:
                q.append([r,c+1])
        return image

s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
