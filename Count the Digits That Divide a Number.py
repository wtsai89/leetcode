class Solution:
    def countDigits(self, num: int) -> int:
        copy = num
        digits = []
        while copy:
            digits.append(copy % 10)
            copy = copy // 10
        
        a = 0
        for i in digits:
            if num % i == 0:
                a += 1
        return a

s = Solution()
print(s.countDigits(7))