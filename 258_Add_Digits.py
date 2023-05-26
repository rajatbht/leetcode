class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
        temp=0
        while num!=0:
            digit=num%10
            temp += digit
            num=num//10
        return self.addDigits(temp)

val=38
b=Solution()
b.addDigits(val)