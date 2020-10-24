"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1
"""

class Solution:
    def coinChange(self, coins, amount):
        #迭代
        d = [amount+1 for i in range(amount+1)]
        d[0]=0
        for s in range(1, amount+1):
            for c in coins:
                if s-c>=0:
                    d[s] = min(d[s],d[s-c]+1)
                else:
                    continue
        if d[-1]==amount+1:
            return -1
        return d[-1]
    def _coinChange(self, coins, amount):
        memo = dict()
        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]
            # base case
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)

            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)

    def change(self,coins,amount):
        #给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
        d=[0]*(amount+1)
        d[0]=1

        for coin in coins:#选项在前，组合数，在内层就是排列数，而这题排列时会出现重复问题
            for i in range(coin,amount+1):
                d[i]+=d[i-coin]
        return d[-1]
coins=[1,2,5]
amount=3