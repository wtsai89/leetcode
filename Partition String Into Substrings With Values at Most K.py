class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans = 0
        curr = 0
        for c in s:
            digit = int(c)
            if digit > k:
                return -1
            curr = curr*10 + digit
            if curr > k:
                curr = digit
                ans += 1
                
        return ans + 1

s = Solution()
print(s.minimumPartition("165462",60))