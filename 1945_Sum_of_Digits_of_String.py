class Solution(object):
    def digitSum(self,num):
        temp=0
        while num!=0:
            remainder=num%10
            temp += remainder
            num = num//10
        return temp
    
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        convert=""
        for i in range(len(s)):
            temp=ord(s[i])-96
            convert += f"{temp}"
        convert=int(convert)
        for i in range(k):
            convert= self.digitSum(convert)
        return convert

s= "zbax"
k=2
b=Solution()
b.getLucky(s,k)