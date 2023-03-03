from typing import List
from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [-1] * n
        provinces = defaultdict(lambda: set())

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    if visited[j] != -1 and visited[j] != i:
                        mergeSet = provinces.pop(visited[j])
                        for p in mergeSet:
                            visited[p] = i
                        provinces[i] = provinces[i].union(mergeSet)
                    else:
                        visited[j] = i
                        provinces[i].add(j)

        return len(provinces)
    
s = Solution()
print(s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))