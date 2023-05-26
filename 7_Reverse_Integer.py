class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            sign=-1
            x=-x
        else:
            sign=1
        temp=0
        while x!=0:
            remainder=x%10
            temp = temp*10+remainder
            x=x//10
        return temp*sign

x=123
b=Solution()
b.reverse(x)