class Solution:
    #完全背包问题
    def max_bag(self,w,v,T):
        # w: list[]
        # v: list[]
        # T: int/target value
        # 
        # max x*p
        # x*w <T
        # x : int
        n=len(w)
        d = [[0 for i in range(T)] for j in range(n)]

        for i in range(n):
            for j in range(T+1):
                d[i][j]=d[i-1][j]
                if w[i]<j:
                    d[i][j] =max(d[i][j],d[i][j-w[i]]+v[i])
        return d[-1][-1]
        
    def _max_bag_v2(self,w,v,T):
        n=len(w)
        d = [[0 for i in range(T+1)] for j in range(2)]

        for i in range(n):
            for j in range(T+1):
                d[i%2][j]=d[0][j] if i%2==1 else d[1][j]
                if w[i]<j:
                    d[i%2][j] =max(d[i%2][j],d[i%2][j-w[i]]+v[i])
        return d[(n-1)%2][-1]
    
    def _max_bag_v3(self,w,v,T):
        n=len(w)
        d = [0 for i in range(T+1)]
        for i in range(n):
            for j in range(w[i],T+1):
                d[j] =max(d[j],d[j-w[i]]+v[i])
        return d[-1]

    def _max_bag_v4(self,w,v,T):
        ##有点像[coinChange.py]的方法，
        n=len(w)
        d = [0 for i in range(T+1)]
        for j in range(T+1):
            for i in range(n):
                if j>w[i]:
                    d[j] =max(d[j],d[j-w[i]]+v[i])
        return d[-1]     