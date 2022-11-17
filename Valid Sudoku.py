from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet, colSet, sqSet = set(), set(), set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                cell = board[i][j]
                if cell == ".":
                    continue
                
                if (i,cell) in rowSet or (j,cell) in colSet or (i//3,j//3,cell) in sqSet:
                    return False
                else:
                    rowSet.add((i,cell))
                    colSet.add((j,cell))
                    sqSet.add((i//3,j//3,cell))
        
        return True

s = Solution()
a = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(s.isValidSudoku(a))