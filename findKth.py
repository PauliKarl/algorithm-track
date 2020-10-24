##找到数组中第K大的数， 使用快排的思想，假设数组中该数一定存在
#[1,3,5,2,2],5,3
#return 2

def findKth(a,n,K):
    left = []
    right = []
    mid = n//2
    midval = a[mid]
    a.pop(mid)

    for i in range(n-1):
        if a[i]<mid:
            left.append(a[i])
        else:
            right.append(a[i])
    
    if len(right)==K-1:
        return midval
    elif len(right)>=K:
        return findKth(right,len(right),K)
    elif len(right)<K-1:
        return findKth(left,len(left),K-len(right)-1)


a = [1,3,5,2,2]
n = 5
K=3
print(findKth(a,n,K))
