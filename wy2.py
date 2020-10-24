
def bfs(target, clist):
    if target==0:
        res.append(clist.copy())
        return
    elif target<0:
        return 
    n = len(clist)
    for i in range(n):
        va=clist[i]
        target-=va
        clist.pop(i)
        bfs(target,clist)
        target+=va
        clist.insert(i,va)

nums = [30,60,5,15,30]
suma = sum(nums)
res = []
rem = 0 
nums.sort()
for i in nums:
    if suma%2==0:
        mid = suma/2
        bfs(mid,nums)
        if len(res)>0:
            for i in res[0]:
                rem+=i
            rem = sum(nums)-2*mid
            print(rem)
            break
    suma-=i
    


bfs(60,nums)
print(res)
