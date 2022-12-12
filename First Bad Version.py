# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        a = [0,0,0,1,1]
        def isBadVersion(n):
            return a[n-1]
        first = 1
        last = n
        
        while first != last:
            mid = (first + last + 1) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                last = mid-1
            else:
                first = mid+1
                
        return first

s = Solution()
print(s.firstBadVersion(5))