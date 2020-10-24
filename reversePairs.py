class Solution:
    def __init__(self):
        self.cnt = 0

    def reversePairs(self, nums):
        self.mergesort(nums)
        return self.cnt

    def mergesort(self,nums):
        '''
        归并排序
            a: 待排序数列表
        return sorted_a 已排序的数组
        '''
        if len(nums)<2:
            return nums
        left, right = [], []
        left = nums[:len(nums)//2]
        right = nums[(len(nums)//2-len(nums)):]
        return self.__merge(self.mergesort(left), self.mergesort(right))
    
    def __merge(self,la, ra):
        arr = []
        while len(la)>0 and len(ra)>0:
            if la[0]<=ra[0]:
                arr.append(la[0])
                la.pop(0)
            else:
                self.cnt+=len(la) ##右边第一个小于左边第一个时，则右边第一个数小于左边所有的数此时逆序对的个数就是左边元素个数
                arr.append(ra[0])
                ra.pop(0)
        arr = arr + la
        arr = arr + ra
        return arr

nums=[7,5,6,4]
so = Solution()
print(so.reversePairs(nums))