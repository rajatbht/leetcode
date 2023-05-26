class Solution(object):
    def digitSquareSum(self,n):
        nextVal=0
        while n!=0:
            temp=n%10
            n=n//10
            nextVal += temp**2
        return nextVal
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow=self.digitSquareSum(n)
        fast=self.digitSquareSum(n)
        fast=self.digitSquareSum(fast)
        while slow!=fast:
            slow=self.digitSquareSum(slow)
            fast=self.digitSquareSum(fast)
            fast=self.digitSquareSum(fast)
        if slow==1:
            return True
        return False
        


val=4
b=Solution()
b.isHappy(val)