from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1

        while top < bottom:
            mid = (top + bottom) // 2
            if target == matrix[mid][len(matrix[0])-1]:
                return True
            elif target < matrix[mid][len(matrix[0])-1]:
                bottom = mid
            else:
                top = mid+1

        left = 0
        right = len(matrix[0])-1

        while left < right:
            mid = (left + right) // 2
            if target == matrix[top][mid]:
                return True
            elif target < matrix[top][mid]:
                right = mid
            else:
                left = mid+1

        if target == matrix[top][left]:
            return True
        return False
s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))