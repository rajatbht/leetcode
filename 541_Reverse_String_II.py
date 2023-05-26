class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s)<=2*k:
            return s
        
        res=""
        self.reverseStr(s[0:2*k],k)
        temp=list(s)
        start=0
        end=k-1
        while start<end:
            temp[start],temp[end]=temp[end],temp[start]
            start += 1
            end -= 1
        temp="".join(temp)
        res+=temp
        return res
        
        
s = "abcdefghijklmnopqrstuvwxyz"
k = 2
b=Solution()
b.reverseStr(s,k)