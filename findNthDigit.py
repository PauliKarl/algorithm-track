class Solution:
    """
    数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
    """
    def findNthDigit(self, n: int) -> int:
        # 首先判断第N个数字属于是几位数，用digits表示
        # 1-9： 9
        # 10-99： 90
        # 100-999： 900
        base = 9
        digits = 1
        while n - base * digits > 0:
            n -= base * digits
            base *= 10
            digits += 1
        # 计算target的值
        idx = n % digits  # 注意由于上面的计算，n现在表示digits位数的第n个数字， idx取值【1，2，..., digits-1, 0】当idx==0时，即最后一位

        # 确定digits位数的首数
        number = 1
        for i in range(1,digits):
            number *= 10
        
        # 计算digits位数的第n个数字
        number = number + (n-1)//digits

        # 找到number中的第idx个数字
        if idx==0:
            return number%10
        else:
            for i in range(digits-idx):
                number//=10
            return number%10