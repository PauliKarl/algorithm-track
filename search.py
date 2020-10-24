"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1

"""
#二分查找
class Solution:
    def search(self, nums, target):
        left = 0 
        right = len(nums)-1

        while left<=right:
            mid = (right-left)//2 + left

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
        return -1
    @staticmethod
    def searchRange(nums, target):
        if len(nums)==0:
            return [-1,-1]
            
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]>=target:
                right = mid-1
            elif nums[mid]<target:
                left = mid +1
        if len(nums)>left and nums[left]==target:
            res_left = left
        else:
            return [-1,-1]

        left = 0
        right = len(nums)-1
        while right>=left:
            mid = left+(right-left)//2
            if nums[mid]>target:
                right = mid-1
            elif nums[mid]<=target:
                left = mid+1     
        if right>=0 and nums[right]==target:
            res_right = right
        else:
            return [-1,-1]
        return [res_left,res_right]

nums = [10]
target = 10

print(Solution.searchRange(nums,target))