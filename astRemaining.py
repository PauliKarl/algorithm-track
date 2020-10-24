class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = [i for i in range(n)]

        for j in range(n-1):
            idx = m%len(nums)
            nums.pop(idx)
        return nums[0]


so=Solution()

print(so.lastRemaining(5,3))
