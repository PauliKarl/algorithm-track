class Solution(object):
    def __init__(self):
        super().__init__()

    def findk(self, nums1, start1, nums2, start2, K):
        if start1>=len(nums1):
            return nums2[start2+K-1]
        if start2>=len(nums2):
            return nums1[start1+K-1]
        if K==1:
            return min(nums1[start1], nums2[start2])
        if len(nums1)<start1+K//2:
            val2K1 = float('inf')
        else:
            val2K1 = nums1[start1+(K//2)-1] 
        if len(nums2)<start2+K//2:
            val2K2 = float('inf')
        else:
            val2K2 = nums2[start2+(K//2)-1]
        if  val2K1>val2K2:
            return self.findk(nums1, start1, nums2, start2+K//2, K-K//2)
        else:
            return self.findk(nums1, start1+K//2, nums2, start2, K-K//2)

    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        head = (m+n+1)//2
        end = (m+n+2)//2
        return (self.findk(nums1, 0, nums2, 0, head)+self.findk(nums1, 0, nums2, 0, end))/2.0


nums1 = [1,2]
nums2 = [3,4]
eva = Solution()
print(eva.findMedianSortedArrays(nums1,nums2))