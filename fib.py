class Solution:
    """
    写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
    斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
    答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
    """
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        lre=2
        dp = [0,1]
        for i in range(2,n):
            dp[i%2]=(sum(dp)%1000000007)
        return sum(dp)%1000000007

##生成器实现
def fib(n):
    x,a,b = 0,0,1
    while n>x:
        yield b
        a,b = b,a+b
        x+=1

fi = fib(10)
for i in fi:
    print(i)