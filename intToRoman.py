class Solution:
    def intToRoman(self, num: int) -> str:
        num10 = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        Rolist = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        str_Ro = []
        for i in range(len(num10)):
            count = num//num10[i]
            num = num - count*num10[i]
            for j in range(count):
                str_Ro.append(Rolist[i])
        
        return "".join(str_Ro)
    def romanToInt(self, s: str) -> int:
        num10 = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        Rolist = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        s_list = list(s)
        num = 0
        while len(s):
            two_c = s[:2]
            one_c = s[0]
            if two_c in Rolist:
                num = num + num10[Rolist.index(two_c)]
                s=s[2:]
            else:
                num = num + num10[Rolist.index(one_c)]
                s=s[1:]
        return num

x=4
so = Solution()
print(so.intToRoman(x))