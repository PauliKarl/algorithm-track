"""
给一个有 n 个结点的有向无环图，找到所有从 0 到 n-1 的路径并输出（不要求按顺序）
二维数组的第 i 个数组中的单元都表示有向图中 i 号结点所能到达的下一些结点（译者注：有向图是有方向的，即规定了a→b你就不能从b→a）空就是没有下一个结点了
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #bfs
        res = []
        path = [0]
        def bfs(path,clist):
            if path[-1]==len(graph)-1:
                res.append(path.copy())
                return
            N=len(clist)
            for i in range(N):
                next_id = clist[i]
                path.append(next_id)
                bfs(path,graph[next_id])
                path.pop()
        bfs(path,graph[0])
        return res