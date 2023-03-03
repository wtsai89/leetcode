class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def p(entry, remaining):
            if remaining:
                for i in range(len(remaining)):
                    p(entry + [remaining[i]], remaining[:i] + remaining[i+1:])
            else:
                ans.append(entry)

        ans = []
        p([], nums)
        return ans