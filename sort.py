class mysort(object):
    def __init__(self):
        super(mysort,self).__init__()
    ##冒泡排序
    def bubble(self,a):
        for i in range(len(a)):
            flag = True
            for j in range(1,len(a)):
                if a[j-1]>a[j]:
                    flag = False
                    a[j-1],a[j] = a[j], a[j-1]
            if flag:
                return a
        return a
    def quick(self,a):
        if len(a)<2:
            return a
        midval = a[len(a)//2]
        a.pop(len(a)//2)
        left = []
        right = []
        for i in range(len(a)):
            if a[i]<midval:
                left.append(a[i])
            else:
                right.append(a[i])
        return self.quick(left) + [midval] + self.quick(right)

    def quicksorted(self, a):
        '''
        快速排序算法
        param:
            a: 待排序数列表
        return sorted_a 已排序的数组
        '''
        if len(a) <2:
            return a
        
        mid_num = a[len(a)//2]
        a.pop(len(a)//2)
        left, right = [], []
        for val in a:
            if val<mid_num:
                left.append(val)
            else:
                right.append(val)
        return self.quicksorted(left)+[mid_num]+self.quicksorted(right)
    def select(self,a):
        if len(a)<2:
            return a
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                if a[j]<a[i]:
                    a[i],a[j] = a[j],a[i]
        return a

    def mergesorted(self, a):
        '''
        归并排序
            a: 待排序数列表
        return sorted_a 已排序的数组
        '''
        if len(a)<2:
            return a
        left, right = [], []
        left = a[:len(a)//2]
        right = a[(len(a)//2-len(a)):]
        return self.__merge(self.mergesorted(left), self.mergesorted(right))
    
    def __merge(self, la, ra):
        arr = []
        while len(la)>0 and len(ra)>0:
            if la[0]<ra[0]:
                arr.append(la[0])
                la.pop(0)
            else:
                arr.append(ra[0])
                ra.pop(0)
        arr = arr + la
        arr = arr + ra
        return arr


a=[5,4,2,7,1,5,9,33,23,9]

so=mysort()

print(so.select(a))



    
    




    