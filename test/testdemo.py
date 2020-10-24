
##
mstr = []
num=False
with open("./test/input.txt",'r') as f:
    for line in f.readlines():
        if not num:
            N, M = list(map(int,line.split()))
            num = True
        else:
            mstr.append(line.strip())


path = []

for i in range(N):
    for j in range(M):
        if mstr[i][j]=='X':
            path.append((i,j))
        elif mstr[i][j]=='T':
            Fx, Fy = i, j

numofX = len(path)
minDis = [float('inf')]*numofX
for t in range(numofX):
    x0,y0 = path[t]
    visited = [[0 for i in range(M)] for j in range(N)]
    d = [[0 for i in range(M)] for j in range(N)]
    ch = [[x0,y0]]
    visited[x0][y0]=1
    
    while len(ch)>0:
        p=len(ch)
        for i in range(p):
            x,y = ch.pop(0)
            if x+1<N and visited[x+1][y]==0 and (mstr[x+1][y]!='1'):
                ch.append([x+1,y])
                d[x+1][y] = d[x][y]+1
                visited[x+1][y] = 1
            if x-1>=0 and visited[x-1][y]==0 and (mstr[x-1][y]!='1'):
                ch.append([x-1,y])
                d[x-1][y] = d[x][y]+1
                visited[x-1][y] = 1
            if y+1<M and visited[x][y+1]==0 and (mstr[x][y+1]!='1'):
                ch.append([x,y+1])
                d[x][y+1] = d[x][y]+1
                visited[x][y+1] = 1
            if y-1>=0 and visited[x][y-1]==0 and (mstr[x][y-1]!='1'):
                ch.append([x,y-1])
                d[x][y-1] = d[x][y]+1
                visited[x][y-1] = 1
        if d[Fx][Fy]>0:
            ch = []
    minDis[t]=d[Fx][Fy]
    del d
    del visited
mindist = float('inf')
flg = False
for k in range(numofX):
    if minDis[k]<mindist:
        mindist=minDis[k]
        flg = True
if not flg:
    print('No')
else:
    print(minDis)
    
    for j in range(numofX):
        if minDis[j]==mindist:
            print(path[j][0],path[j][1],end=" ")


