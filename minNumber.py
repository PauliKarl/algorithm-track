class Solution:
    """
    输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
    """
    def minNumber(self, nums):
        """
        利用排序算法，这里选择快排
        排序的传递性：xy<yx and yz<zy, so xz<zx
        证明:
            x: a位数
            y: b位数
            z：c位数
            由xy<yx and yz<zy可知：
            x*(10**b) +y <y*(10**a)+x and y*(10**c) +z <z*(10**b)+y
            x*(10**b-1)<y*(10**a-1) and y*(10**c-1)<z*(10**b-1)
            后式代入前式：
            x*(10**b-1)<z*(10**b-1)/(10**c-1) * (10**a-1)

            所以x*(10**c-1)<z*(10**a-1)
            so:
                x*10**c + z < z*10**a + x
        """        
        def faster_sorted(arr):
            left = []
            right = []
            if len(arr)<2:
                return arr
            minnum = arr[len(arr)//2]
            arr.pop(len(arr)//2)
            for i in range(len(arr)):
                if int(str(arr[i])+str(minnum))<int(str(minnum)+str(arr[i])):
                    left.append(arr[i])
                else:
                    right.append(arr[i])
            return faster_sorted(left) + [minnum] + faster_sorted(right)
        nums_sorted = faster_sorted(nums)

        return "".join([str(s) for s in nums_sorted])

res = Solution()

nums=[10,2]
print(res.minNumber(nums))
