class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
                    '(':')',
                    '[':']',
                    '{':'}'
                }
        q = []
        
        for c in s:
            if c in valid:
                q.append(valid[c])
            elif not q or c != q.pop():
                return False
        
        if q:
            return False
        return True

s = Solution()
print(s.isValid("()[]{}"))