from typing import List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(i, visited):
            if visited[i]:
                return
            visited[i] = True
            stone = stones[i]
            for j in range(len(stones)):
                if stone[0] == stones[j][0] or stone[1] == stones[j][1]:
                    dfs(j, visited)

        coll = 0
        visited = [False] * len(stones)
        for i in range(len(stones)):
            if not visited[i]:
                dfs(i, visited)
                coll += 1

        return len(stones) - coll