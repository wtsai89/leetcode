class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                nindex = 1
                flag = 1
                for j in range(i+1,i+len(needle)):
                    if haystack[j] != needle[nindex]:
                        flag = 0
                        break
                    nindex += 1
                if flag:
                    return i
                
        return -1

s = Solution()
h = "sadbutsad"
n = "sad"
print(s.strStr(h,n))