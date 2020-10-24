class Solution:
    """
    请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
    在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
    """
    def isMatch(self, s: str, p: str) -> bool:
        s, p = '#'+s, '#'+p #避免初始空字符的复杂判断
        m, n = len(s), len(p)
        dp = [[False]*n for _ in range(m)] #初始化动态规划的辅助数组
        dp[0][0] = True #都是空字符的时候，返回True
        
        for i in range(m):
            for j in range(1, n):
                if i == 0:
                    dp[i][j] = j > 1 and p[j] == '*' and dp[i][j-2] # 当j>1，i=0时， p[j]="*",直接去掉正则符“—*”，dij取决于di[j-2]
                elif p[j] in [s[i], '.']: # i>0时，如果 p[j]==s[i],或者p[j]=".", dp[i][j] = dp[i-1][j-1]
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*': #i>0时， p[j]="*"有两种情况，（1）0次循环：直接去掉正则符“—*”，dij取决于di[j-2]，（2）多次循环p[j-1] in [s[i], '.'] and dp[i-1][j]
                    dp[i][j] = j > 1 and dp[i][j-2] or p[j-1] in [s[i], '.'] and dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]