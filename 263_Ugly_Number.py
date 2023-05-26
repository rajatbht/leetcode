class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        for i in 2,3,5:
            while n%i==0:
                n=n//i
        return n==1
        # if n<1:
        #     return False
        # while n!=1:
        #     if n%2==0:
        #         n=n//2
        #     elif n%3==0:
        #         n=n//3
        #     elif n%5==0:
        #         n=n//5
        #     else:
        #         return False
        # return True

n=14
b=Solution()
b.isUgly(n)