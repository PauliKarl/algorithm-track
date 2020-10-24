class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        SumClosest = nums[0]+nums[1]+nums[2]
        
        for i in range(len(nums)):
            R = len(nums)-1
            L = i+1
            while L<R:
                res = target-(nums[i]+nums[L]+nums[R])
                if res==0:
                    return target
                elif res>0:
                    L=L+1
                else:
                    R=R-1
                if abs(res)<abs(SumClosest-target):
                    SumClosest=abs(target-res)
        
        return SumClosest

nums = [1,2,4,8,16,32,64,128]


target = 82

so = Solution()

print(so.threeSumClosest(nums, target))