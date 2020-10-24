##一个集合的所有子集

#s顺时针矩形填数字

def ismatch(count):
    if count%10==7 and (count//10)%2==1:
        return True
    return False

def getMatrix(M,N):
    #M:row
    #N:col
    ma = [[0 for i in range(N)]for i in range(M)]
    count = 1
    x0,y0 = 0,0 
    xn,yn = M-1,N-1
    while x0<=xn and y0<=yn:
        for i in range(y0,yn+1):
            ma[x0][i] = count
            if ismatch(count):
                 res.append([x0,i])
            count+=1
        for i in range(x0+1,xn+1):
            ma[i][yn] = count
            if ismatch(count):
                 res.append([i,yn])
            count+=1
        if xn>x0:#非单行
            for i in range(yn-1,y0-1,-1):
                ma[xn][i] = count
                if ismatch(count):
                    res.append([xn,i])
                count+=1
        if yn>y0:
            for i in range(xn-1,x0,-1):
                ma[i][y0] = count
                if ismatch(count):
                    res.append([i,y0])
                count+=1
        x0+=1
        y0+=1
        xn-=1
        yn-=1
    return ma

M,N=10,10
res=[]
if M<10 or N<10 or M>1000 or N>1000: 
    print(res)
else:
    getMatrix(M,N)

    print(res)


####
#二叉树有n个节点，每个节点的深度已知（代码中depth），让你计算该树总共有多少种可能的形状。
import os
 
n = int(input())
depth = [int(d) for d in input().split()]
 
M = 10 ** 9 + 7
 
 
def combination(n, k):
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
 
    top = 1
    for i in range(n, n - k, -1):
        top *= i
 
    down = 1
    for i in range(1, k + 1):
        down *= i
 
    return (top // down) % M
 
 
def helper():
    if n == 0:
        return 0
 
    max_depth = max(depth)
    depth_count = [0] * (max_depth + 1)
 
    for d in depth:
        depth_count[d] += 1
 
    for i in range(max_depth):
        if 2 * depth_count[i] < depth_count[i + 1]:
            return 0
 
    r = 1
    for i in range(1, max_depth + 1):
        r *= combination(2 * depth_count[i - 1], depth_count[i])
        r %= M
 
    return r
 
 
print(helper())