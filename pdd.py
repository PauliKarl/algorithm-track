class Solution:
    #  问题参照图像(pdd4.png)
    def solveNQueens(self, P):
        self.num = 0
        self.path = P
        self.loc = []
        ##先把需要种植位置记录下来，然后回溯
        for i in range(1,7):
            for j in range(1,7):
                if self.path[i][j]=="#":
                    self.loc.append((i,j))

        self.backtrack(self.loc)

        return self.num


    def isOk(self,idx, col, row):
        ##判断位置[row][col]是否可以防止皇后
        if self.path[row][col]=="*":
            return False
        if self.path[row-1][col]!=idx and self.path[row][col-1]!=idx and self.path[row+1][col]!=idx and self.path[row][col+1]!=idx:
            return True
        return False
    def backtrack(self,path):
        ##找到所有答案
        if len(path)==0:
            self.num+=1
            return
        for x in range(1,7):#每个位置6种植物
            (i,j) = path.pop()
            if self.isOk(x, j, i):
                self.path[i][j]=x
                self.backtrack(path)
                self.path[i][j]="#"
            path.append((i,j))



#D=["99999999","9#*****9","9*#****9","9******9","9******9","9******9","9******9","99999999"]
D=['#*****',"*#****","******","******","******","******"]

D = ["9" + d + "9" for d in D]
ex_D = ["99999999"]
ex_D.extend(D)
ex_D.append("99999999")

P=[list(d) for d in ex_D]
so=Solution()

print(so.solveNQueens(P))