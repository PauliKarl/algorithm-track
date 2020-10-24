arr = [3,2,1,0,4]

n=len(arr)
d = [0]*n
d[-1]=1
for i in range(n):
    #id = n-i-1
    for k in range(arr[n-i-1]):
        if (n-i+k)<n and d[n-i+k]==1:
            d[n-i-1]=1
            break
if d[0]==0:
    print("false")
else:
    print("true")