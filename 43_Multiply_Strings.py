class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        pointer1 = 1
        pointer2 = 1
        n1=ord(num1[0]) - ord("0")
        n2=ord(num2[0]) - ord("0")
        while pointer1 <= len(num1)-1 or pointer2 <= len(num2)-1:
            if pointer1 <= len(num1)-1:
                v1=num1[pointer1]
                v1=ord(v1) - ord("0")
                n1= n1*10 + v1
                pointer1 +=1
            if pointer2 <= len(num2)-1:
                v2=num2[pointer2]
                v2=ord(v2) - ord("0")
                n2= n2*10 + v2
                pointer2 +=1
            
            # carry, val = divmod(v1 * v2 + carry , 10)
            # result = str(val) + result
        return str(n1*n2)

num1 = "11"
num2 = "123"
a=Solution()
a.multiply(num1,num2)