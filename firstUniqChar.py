class Solution:
    """
    在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
    """
    def firstUniqChar(self, s: str) -> str:
        res = []
        multi = []
        for t in s:
            if t not in res and t not in multi:
                res.append(t)
            elif t in res:
                multi.append(res.pop(res.index(t)))
        if len(res)==0:
            return " "
        else:
            return res[0]