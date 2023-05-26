class Solution(object):
    dp={}
    def fib(self, n):
        if n in self.dp:
            return self.dp[n]
        if n==0:
            return 0
        if n==1:
            return 1
        res = self.fib(n-1)+self.fib(n-2)
        self.dp[n] = res
        return res
        

n = 5
b=Solution()
b.fib(n)