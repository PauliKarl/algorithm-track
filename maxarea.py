class Solution:
    def maxArea(self, height: List[int]) -> int:
        #双指针法
        Area = []
        while len(height)>1:
            Area.append(min(height[0],height[-1])*(len(height)-1))
            if height[0]>height[-1]:
                height.pop(-1)
            else:
                height.pop(0)
        return max(Area)