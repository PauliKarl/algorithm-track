class Solution:
    def translateNum(self, num: int) -> int:
        ##0-25 第i位可以和第i-1项连起来，第i位单独算
        if num <10:
            return 1
        d = [1,1]
        digits = len(str(num))

        for i in range(2,digits+1):
            if 10<=num%100<=25:
                d[i%2] = sum(d)
            else:
                d[i%2] = d[(i+1)%2]
            num=num//10
        return max(d)

res = Solution()

num=1228
print(res.translateNum(num))
