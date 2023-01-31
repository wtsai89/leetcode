from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rmat = len(mat)
        cmat = len(mat[0])
        if rmat * cmat != r * c:
            return mat
        lmat = []
        for i in range(rmat):
            for j in range(cmat):
                lmat.append(mat[i][j])

        ans = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(lmat.pop(0))
            ans.append(row)

        return ans

s = Solution()
print(s.matrixReshape([[1,2],[3,4]],1,4))
