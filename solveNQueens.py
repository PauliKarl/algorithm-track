import copy
class Solution:    
    def solveNQueens(self, n):
        self.res = []
        path = [["." for i in range(n)] for i in range(n)]
        self.backtrack_find0ne(path,0)

        return [["".join(row) for row in ele] for ele in self.res]
    def isOk(self,path, col, row):
        ##判断位置[row][col]是否可以防止皇后
        if row==0:
            return True
        #检查列是否满足
        for ele in path[:row]:
            if ele[col]=="Q":
                return False
        #检查左上是否满足
        L_row=row-1
        L_col=col-1
        while L_row>-1 and L_col>-1:
            if path[L_row][L_col]=="Q":
                return False
            L_row=L_row-1
            L_col=L_col-1
        #检查右上是否满足r
        R_row=row-1
        R_col=col+1
        while R_row>-1 and R_col<len(path):
            if path[R_row][R_col]=="Q":
                return False
            R_row=R_row-1
            R_col=R_col+1
        return True
    def backtrack(self,path,row):
        ##找到所有答案
        if row==len(path):
            self.res.append(copy.deepcopy(path))
            return
        for i in range(len(path)):#col
            path[row][i] = "Q"
            if self.isOk(path, i, row):
                self.backtrack(path, row+1)
                path[row][i]="."
            else:
                path[row][i]="."
                continue
    def backtrack_find0ne(self,path,row):
        ##找到一个答案
        if row==len(path):
            self.res.append(copy.deepcopy(path))
            return True
        for i in range(len(path)):#col
            path[row][i] = "Q"
            if self.isOk(path, i, row):
                if self.backtrack_find0ne(path, row+1):
                    return True
                path[row][i]="."
            else:
                path[row][i]="."
                continue   
        return False         

n=4
so = Solution()
print(so.solveNQueens(n))