class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        #dfs
        self.minAP = []
        deta = [(0,1),(1,0)]
        step = 2*(len(dungeon)-1)
        curminAP = 100000
        def dfs(curminAP,AP,x,y):
            curminAP = min(curminAP,AP)
            if x==len(dungeon)-1 and y==len(dungeon[0])-1:
                self.minAP.append(curminAP)
                return
            for dx,dy in deta:
                if x+dx<len(dungeon) and y+dy<len(dungeon[0]):
                    AP = AP+dungeon[x+dx][y+dy]
                    dfs(curminAP,AP,x+dx,y+dy)
                    AP = AP-dungeon[x+dx][y+dy]
        dfs(curminAP,dungeon[0][0],0,0)

        if max(self.minAP)<=0:
            return 1-max(self.minAP)
        else:
            return 1
    #倒推动态规划，倒推的base问题是已知答案D[i][j]的值表示从i，j位置到达右下角的最小生命值
    def _calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        BIG = 10**9
        dp = [[BIG] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)
        return dp[0][0]



nums=[[0,-3]]
so=Solution()
print(so.calculateMinimumHP(nums))