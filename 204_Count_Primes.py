class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        if n==3:
            return 1
        count=1
        for i in range(4,n):
            j=2
            while j*j <= i:
                if i%j!=0:
                    count += 1
                    break
                j += 1
        return count +1

n=10
a=Solution()
a.countPrimes(n)
# 123456