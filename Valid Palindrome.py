
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ("".join(c for c in s if c.isalpha() or c.isdigit())).lower()
        if s == s[::-1]:
            return True
        return False
sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))