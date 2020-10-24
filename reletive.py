class Solution:
    def reletive_7(self , digit ):
        # write code here
        c, res = digit, []
        def dfs(x):
            if x == len(c) - 1:
                res.append(c.copy())
                return
            dic = list()
            for i in range(x, len(c)):
                dic.append(c[i])
                c[i], c[x] = c[x], c[i]
                dfs(x + 1) 
                c[i], c[x] = c[x], c[i]
        dfs(0)
        
        num=0
        for a in res:
            le = len(a)
            nn=0
            for i in range(len(a)):
                nn=nn*10+a[i]
            if nn%7==0:
                num+=1
        return num


digit = [1,1,2]

so=Solution()
print(so.reletive_7(digit))