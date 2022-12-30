class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        binary = bin(x^y)
        ones = ''.join(x for x in binary if x == '1')
        return len(ones)

s = Solution()
print(s.hammingDistance(1,4))