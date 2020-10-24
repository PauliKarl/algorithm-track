class Solution:
    """
    输入一个字符串，打印出该字符串中字符的所有排列。
    你可以以任意顺序返回这个字符串数组，但里面不能有重复元素
    """
    def permutation(self, s):
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c)) # 添加排列方案
                return
            dic = list()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.append(c[i])
                c[i], c[x] = c[x], c[i] # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1) # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i] # 恢复交换
        dfs(0)
        return res
    
    def permute(self, nums):
        self.res=[]
        self.backtrack([],nums)
        return self.res


    def backtrack(self,path,renums):
        if len(renums)==0:
            self.res.append(path.copy()) ##使用copy（）否则局部变量path会随之改变，影响结果
            return
        for i in range(len(renums)):
            tmp = renums.pop(i)
            path.append(tmp)
            self.backtrack(path,renums)
            path.pop()
            renums.insert(i,tmp)


nums=[1,2,3]
so = Solution()

print(so.permute(nums))

