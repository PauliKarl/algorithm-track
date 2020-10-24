mstr = ["1111#","1#11#", "1111#", "1#11#", "1111#"]

loc = [1,0,4,3]
[x0,y0,x1,y1] = loc
n = 5

d = [[0 for i in range(n)] for j in range(n)]
visited= [[0 for i in range(n)] for j in range(n)]
d[x0][y0] = 1
visited[x0][y0]=1
disable = ["#","@"]
ch = []
ch.append([x0,y0])

while len(ch)>0:
    p=len(ch)
    for i in range(p):
        x,y = ch.pop(0)
        if x+1<n and visited[x+1][y]==0 and (mstr[x+1][y] not in disable):
            ch.append([x+1,y])
            d[x+1][y] = d[x][y]+1
            visited[x+1][y] = 1
        if x-1>=0 and visited[x-1][y]==0 and (mstr[x-1][y] not in disable):
            ch.append([x-1,y])
            d[x-1][y] = d[x][y]+1
            visited[x-1][y] = 1
        if y+1<n and visited[x][y+1]==0 and (mstr[x][y+1] not in disable):
            ch.append([x,y+1])
            d[x][y+1] = d[x][y]+1
            visited[x][y+1] = 1
        if y-1>=0 and visited[x][y-1]==0 and (mstr[x][y-1] not in disable):
            ch.append([x,y-1])
            d[x][y-1] = d[x][y]+1
            visited[x][y-1] = 1
print(d[x1][y1]-1) 
