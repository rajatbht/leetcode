class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1 or n==3:
            return True
        if n%3==0 or (n-1)%3==0:
            return self.checkPowersOfThree(n//3)
        return False
n = 91
b=Solution()
b.checkPowersOfThree(n)