class Solution:
    """
    在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
    """
    def maxValue(self, grid: List[List[int]]) -> int:
        """
        动态规划，d[i][j] 与递推的公式：
                max(d[i][j-1],d[i-1][j]) + grid[i][j]    i>0 and j>0
                先就i=0火j==0情况初始化，避免了矩阵过大时每次循环内都要判断
        """
        m = len(grid)
        n = len(grid[0])
        d = [[0 for i in range(n)] for j in range(m)]
        
        if m*n==1:
            return grid[0][0]
        d[0][0]=grid[0][0]

        for i in range(1,m):
            d[i][0] = d[i-1][0]+grid[i][0] 
        for j in range(1,n):
            d[0][j] = d[0][j-1] + grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                d[i][j] = max(d[i-1][j],d[i][j-1]) + grid[i][j]
        return d[-1][-1]