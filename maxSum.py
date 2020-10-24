def maxsum(arr):
    if len(arr)==0:
        return 0
    if len(arr)==1:
        return max(0,arr[0])
    excl = 0
    incl = arr[0]

    for i in range(1,len(arr)):

        excl_new = max(excl,incl)
        incl = excl + arr[i]

        excl = excl_new
    return max(excl,incl)


arr = [3,-2,7,-10]
print(maxsum(arr))

