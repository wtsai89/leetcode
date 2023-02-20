from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix)-1
        while top < bot:
            mid = (top + bot) // 2
            if target > matrix[mid][len(matrix[0])-1]:
                top = mid + 1
            else:
                bot = mid

        left, right = 0, len(matrix[0])-1
        while left < right:
            mid = (left + right) // 2
            if target == matrix[top][mid]:
                return True
            elif target < matrix[top][mid]:
                right = mid - 1
            else:
                left = mid + 1

        if target == matrix[top][left]:
            return True
        return False 
s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))