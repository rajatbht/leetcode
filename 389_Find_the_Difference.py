class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s)==0:
            return t
        res={}
        for i in s:
            if i not in res:
                res[i]=1
            else:
                res[i] +=1
        for i in t:
            if i not in res:
                return i
            if res[i]<0:
                return i
            res[i] -=1

s = "abcd"
t = "abcde"
b=Solution()
b.findTheDifference(s,t)