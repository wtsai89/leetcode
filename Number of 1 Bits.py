class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        ones = ''.join(x for x in binary if x == '1')
        return len(ones)

s = Solution()
print(s.hammingWeight(11))