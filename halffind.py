def half_find_left(arr, val):
    left = 0
    right = len(arr)
    flag = False
    while left<right:
        mid = (left+right)//2
        if arr[mid]==val:
            flag = True
            right = mid
        elif arr[mid]>val:
            right = mid
        elif arr[mid]<val:
            left = mid+1
    if flag:
        return left
    else:
        return -1

def half_find_right(arr, val):
    left = 0
    right = len(arr)
    flag = False
    while left<right-1:
        mid = (left+right)//2
        if arr[mid]==val:
            flag = True
            left = mid
        elif arr[mid]>val:
            right = mid
        elif arr[mid]<val:
            left = mid+1
    if flag:
        return left
    else:
        return -1

arr = [1,2,3,4,4,4,4,6,7,8,9]
val = 9
print(half_find_left(arr,val))
print(half_find_right(arr,val))