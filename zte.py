so = []
def backstrack(res, chs, xx, n):
    if res<=0:
        so.append(n-len(chs))
        return
    if chs==0:
        return
    N=len(chs)
    
    for i in range(N):
        xxi=xx[i]
        chi=chs[i]
        N-=1
        xxi = xx.pop(i)
        chi = chs.pop(i)
        if res>xxi:
            res=res-chi
            backstrack(res,chs,xx, n)
            res=res+chi
        else:
            res=res-2*chi
            backstrack(res,chs,xx, n)
            res=res+2*chi
        chs.insert(i,chi)
        xx.insert(i,xxi)
'''            
T=int(input())
for i in range(T):
    line =list(map(int,input().split()))
    n,m = line[0],line[1]
    a=[0]*n
    x=[0]*n
    for i in range(n):
        line =list(map(int,input().split()))
        a[i],x[i]=line[0],line[1]
    so=[]
    backstrack(m,a,x, n)
    if len(so)==0:
        print('-1')
    else:
        print(min(so))
    del a
    del x        

'''

#test
n,m = 3, 100
a=[10, 45, 5]
x=[20, 84, 40]
so=[]
backstrack(m,a,x, n)
if len(so)==0:
    print('-1')
else:
    print(min(so))
del a
del x
