from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        i = 0
        length = len(asteroids)
        while i < length:
            while i < length and res and res[-1] > 0 and asteroids[i] < 0:
                if res[-1] > abs(asteroids[i]):
                    i += 1
                elif res[-1] < abs(asteroids[i]):
                    res.pop()
                else:
                    res.pop()
                    i += 1
            if i < length:
                res.append(asteroids[i])
                i += 1
        return res

s = Solution()
print(s.asteroidCollision([5,10,-5]))