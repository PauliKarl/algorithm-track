"""
你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同
"""
class Solution:
    def numOfWays(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 12
        numabc = 6
        numaba = 6
        for i in range(2,n+1):
            numaba,numabc = 3*numaba+2*numabc,2*(numaba+numabc)
        return (numabc+numaba)%1000000007