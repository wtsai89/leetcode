class Solution:
    def reverseBits(self, n: int) -> int:
        reverseBin = (bin(n)[2:])[::-1]
        reverseBin = reverseBin + ("0"*(32-len(reverseBin)))
        return int(reverseBin,2)

s = Solution()
print(s.reverseBits(int('00000010100101000001111010011100',2)))