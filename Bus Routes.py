from collections import defaultdict
from typing import List
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stopRoutes = defaultdict(lambda: [])
        
        for i in range(len(routes)):
            for stop in routes[i]:
                stopRoutes[stop].append(i)

        visited = set()
        q = [source]
        ans = 0
        while q:
            for _ in range(len(q)):
                at = q.pop(0)
                if at == target:
                    return ans
                for route in stopRoutes[at]:
                    if route not in visited:
                        visited.add(route)
                        q += routes[route]
            ans += 1

        return -1

s = Solution()
print(s.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]],15,12))