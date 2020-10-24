"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res
    def generateParenthesis_dp(self, n):
        d = [[] for i in range(n+1)]
        d[0]=[""]
        for i in range(1,n+1):
            for p in range(i):
                l1 = d[p]
                l2 = d[i-p-1]
                for x in l1:
                    for y in l2:
                        d[i].append("({}){}".format(x,y))
    
        return d[n]  