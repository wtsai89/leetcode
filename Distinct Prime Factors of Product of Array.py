import math
from typing import List
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # get primes between 2 and 1000
        primes = [n for n in range(1001)]
        rangeEnd = math.ceil(math.pow(1000, 0.5))+1
        for i in range(2, rangeEnd):
            if i != 0:
                for j in range((int)(math.pow(i,2)), 1001, i):
                    primes[j] = 0
        primes = [n for n in primes[2:] if n != 0]
        
        #distinct primes
        s = set()
        for i in nums:
            while i > 1:
                for p in primes:
                    while i % p == 0:
                        s.add(p)
                        i = i // p
        return len(s)

s = Solution()
print(s.distinctPrimeFactors([2,4,3,7,10,6]))