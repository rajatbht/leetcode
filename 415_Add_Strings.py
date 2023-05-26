class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result=""
        pointer1 = len(num1)-1
        pointer2 = len(num2)-1
        carry=0
        while pointer1>= 0 or pointer2>= 0 or carry!=0:
            v1=v2=0
            if pointer1>= 0:
                v1=num1[pointer1]
                pointer1 -=1
            if pointer2>= 0:
                v2=num2[pointer2]
                pointer2 -=1
            carry, val = divmod(int(v1) + int(v2) + carry , 10)
            result = str(val) + result
        return result
num1 = "11"
num2 = "123"
a=Solution()
a.addStrings(num1,num2)