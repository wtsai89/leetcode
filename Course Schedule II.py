from typing import List
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: [])
        for c, p in prerequisites:
            graph[c].append(p)
        
        def visit(i, temp):
            if i in ans:
                return 0
            if i in temp:
                return 1
            
            temp.add(i)

            for p in graph[i]:
                f = visit(p, temp)
                if f:
                    return 1
            
            temp.remove(i)
            ans.append(i)
            return 0

        ans = []
        classes = [i for i in range(numCourses)]
        for i in classes:
            flag = visit(i, set())
            if flag:
                return []

        return ans
    
s = Solution()
print(s.findOrder(2,[[1,0]]))
