##最大重叠区间数
nums = [(2,7),(7,9),(11,12)]


#nums.sort(key=lambda x:x[1]) #利用nums[i][1]个元素排序

#自定义比较函数

def comp(x, y):
    if x < y:
        return 1
    elif x > y:
        return -1
    else:
        return 0
nums = [3, 2, 8 ,0 , 1]
nums.sort(comp)
print(nums) # 降序排序[8, 3, 2, 1, 0]
