def swap(lis):
    tmp = lis[0]
    lis[0] = lis[1]
    lis[1] = tmp
lis = [1,2]
swap(lis)
print(lis)