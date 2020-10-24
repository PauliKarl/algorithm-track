class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i=0
        curid=0
        while i<n:
            i+=1
            if nums[curid]==val:
                nums.pop(curid)
            else:
                curid+=1
        return len(nums)