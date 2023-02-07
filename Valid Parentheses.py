class Solution:
    def isValid(self, s: str) -> bool:
        openers = {
                    '(': ')',
                    '{': '}',
                    '[': ']',
                  }

        stack = []
        for i in s:
            if i in openers:
                stack.append(openers[i])
            else:
                if not stack or stack.pop() != i:
                    return False
        if stack:
            return False
        return True

s = Solution()
print(s.isValid("()[]{}"))