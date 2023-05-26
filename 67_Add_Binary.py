class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        pointer1=len(a)-1
        pointer2=len(b)-1
        carry=0
        result=""
        while pointer1 >= 0 or pointer2 >= 0 or carry != 0:
            v1=v2=0
            if pointer1>=0:
                v1=ord(a[pointer1])-ord("0")
                pointer1 -=1
            if pointer2>=0:
                v2=ord(b[pointer2])-ord("0")
                pointer2 -=1
            if v1==1 and v2==1:
                carry , val = divmod(10+carry ,10)
                result = str(val)+result
            elif (v1==1 or v2==1) and carry==1:
                carry , val = divmod(10 ,10)
                result = str(val)+result
            else:
                carry , val = divmod(v1+v2+carry ,10)
                result = str(val)+result
        return result
a = "1"
b = "0"

give=Solution()
give.addBinary(a,b)