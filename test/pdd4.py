N=3
M=5

##用1x1和2x2的木板铺矩阵，有多少种铺发

##先算宽度为2的矩阵大小
L=max(N,M)
H=min(N,M)
dl = [0]*L
dl[0]=1#为了方便初始化
dl[1]=2

for i in range(2,L):
    dl[i] = dl[i-1]+dl[i-2]

#在计算长度扩展
dh = [0]*H
dh[0]=1
dh[1]=dl[-1]

for j in range(2,H):
    dh[j]=dh[j-1]+dh[j-2]*(dl[-1]-1)

print(dh[-1])