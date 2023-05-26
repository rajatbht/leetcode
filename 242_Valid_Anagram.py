class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dict1={}
        for i in s:
            if i not in dict1:
                dict1[i] =1
            else:
                dict1[i] +=1
        for j in t:
            if j not in dict1:
                return False
            if dict1[j]<0:
                return False
            dict1[j] -=1
        return True
        

s = "ac"
t = "bb"
b=Solution()
b.isAnagram(s,t)