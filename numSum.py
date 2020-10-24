class Solution:
    def threeSum(self, nums):
        nums.sort()
        T_num = []
        n=len(nums)
        if n<3:
            return T_num
        for i in range(n):
            if nums[i]>0:
                return T_num

            #从第二个开始，遇到重复数值，直接跳过
            if i>0 and nums[i]==nums[i-1]:
                continue
            L=i+1
            R=n-1
            while L<R:
                if nums[i] + nums[L] + nums[R] == 0:
                    T_num.append([nums[i],nums[L],nums[R]])

                    ##此下两个while解决数值数值重复的问题，遇到重复数值，跳过即可
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    
                    R=R-1
                    L=L+1
                elif nums[i] + nums[L] + nums[R]>0:
                    R=R-1
                else:
                    L=L+1
        return T_num

    def fourSum(self, nums, target):
        nums.sort()
        n=len(nums)
        F_NUM = []
        if n<4:
            return F_NUM
        for t in range(n):
            if 4*nums[t]>target:
                return F_NUM
            if t>0 and nums[t]==nums[t-1]:
                continue
            for i in range(t+1,n):
                if i>t+1 and nums[i]==nums[i-1]:
                    continue
                L=i+1
                R=n-1
                while L<R:
                    if nums[i] + nums[L] + nums[R] == target-nums[t]:
                        F_NUM.append([nums[t],nums[i],nums[L],nums[R]])
                        while(L<R and nums[L]==nums[L+1]):
                            L=L+1
                        while(L<R and nums[R]==nums[R-1]):
                            R=R-1
                        R=R-1
                        L=L+1
                    elif nums[i] + nums[L] + nums[R]>target-nums[t]:
                        R=R-1
                    else:
                        L=L+1
        return F_NUM



nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]

numsf=[0,0,0,0]

so = Solution()
print(so.fourSum(nums))