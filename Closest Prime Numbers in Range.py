import math
from typing import List
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(n):
            if n < 2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        
        q = []
        ans = [-1,-1]
        minimum = 1000000
        for i in range(left,right+1):
            if isPrime(i):
                q.append(i)
                if len(q) > 1:
                    diff = q[1]-q[0]
                    if diff <= 2:
                        return [q[0],q[1]]
                    if diff < minimum:
                        minimum = diff
                        ans = [q[0],q[1]]
                    q.pop(0)
        return ans

s = Solution()
print(s.closestPrimes(10,19))