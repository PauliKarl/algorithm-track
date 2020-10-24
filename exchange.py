class Solution:
    """
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
    """
    def exchange(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return nums
        head = 0
        end =len(nums)-1
        while head<end+1:
            if nums[head]%2==0 and nums[end]%2==1:
                temp = nums[head]
                nums[head]=nums[end]
                nums[end]=temp
                head+=1
                end-=1
            elif nums[head]%2==1:
                head+=1
            elif nums[end]%2==0:
                end-=1
        return nums

