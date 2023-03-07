# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(n):
    a = [0,0,0,1,1]
    return a[n-1]

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                if mid == 1 or not isBadVersion(mid-1):
                    return mid
                right = mid-1
            else:
                left = mid+1
        return left

s = Solution()
print(s.firstBadVersion(5))