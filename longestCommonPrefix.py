class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        prefix_max = ""
        maxFlag = False
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if len(strs[j])<i+1:
                    maxFlag = True
                    continue
                if strs[j][i]!=strs[0][i]:
                    return prefix_max
            if maxFlag:
                return prefix_max
            prefix_max+=strs[0][i]        
        return prefix_max



s=["b","a"]

so = Solution()

print(so.longestCommonPrefix(s))