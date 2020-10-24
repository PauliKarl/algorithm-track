class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        Res = ""
        MaxLen = 0
        for idx in range(len(s)-1):
            distlen = self.findcenterlist(s, idx, idx)
            if s[idx]==s[idx+1]:
                distlen_h = self.findcenterlist(s, idx, idx+1)
            else:
                distlen_h=-1

            if MaxLen<2*distlen+1:
                Res = s[idx-distlen:idx+distlen+1]
                MaxLen = 2*distlen+1
            if MaxLen<2*distlen_h+2:
                Res = s[idx-distlen_h:idx+distlen_h+2]
                MaxLen = 2*distlen_h+2
        return Res

    #回文字符串的中心，这是情况有两种，aba/abba
    def findcenterlist(self, s, i, j):
        n=0
        for n in range(min(i,len(s)-1-j)+1):
            if s[i-n] is not s[j+n]:
                return n-1
        return n

s="bbb"
eva = Solution()
print(eva.longestPalindrome(s))