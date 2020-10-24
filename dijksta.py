##最短路径算法dijkstra迪科斯彻算法使用了广度优先搜索解决赋权有向图或者无向图的单源最短路径问

def difkstra(dist,n):
    '''
    paras:
        dist: distance matrix
        n : start vertex 
    '''
    visited = []
    N=len(dist)
    #记录从n顶点到其他点的最小距离
    D = [0 for i in range(N)]
    D = dist[n] # init distance[i][k]
    D[n] = 0 

    #记录顶点n到其他点最近的路径
    path = [[n,i] for i in range(N)]
    visited.append(n)
    for k in range(N-1):
        #找到当前距离距离顶点n最近的点
        mindis = float('inf')
        minidx = n
        for i in range(N):
            if i in visited:
                continue
            else:
                if mindis>D[i]:
                    mindis = D[i]
                    minidx = i
        #没有到顶点n的联通点了
        if mindis==float('inf'):
            continue
        #加入已访问集合

        visited.append(minidx)

        #寻找minidx顶点的出度，后驱顶点集合
        choice = []
        for i in range(N):
            if i in visited:
                continue
            else:
                if dist[minidx][i]<float('inf'):
                    choice.append(i)
        #广度搜索
        for i in range(len(choice)):
            if dist[n][minidx]+dist[minidx][choice[i]]<D[choice[i]]:
                D[choice[i]] = dist[n][minidx]+dist[minidx][choice[i]]
                path[choice[i]]=path[minidx].copy()
                path[choice[i]].append(choice[i])
        del choice
    return D,path


dist = [[float('inf'),float('inf'),10,float('inf'),30,100],\
        [float('inf'),float('inf'),5,float('inf'),float('inf'),float('inf')],
        [float('inf'),float('inf'),float('inf'),50,float('inf'),float('inf')],\
        [float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),10],\
        [float('inf'),float('inf'),float('inf'),20,float('inf'),60],\
        [float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf')]]

D,P=difkstra(dist,0)
print(D)
print(P)