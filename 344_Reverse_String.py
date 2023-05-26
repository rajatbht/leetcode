class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        start=0
        end=len(s)-1
        while start<end:
            s[start],s[end]=s[end],s[start]
            start +=1
            end -=1
        return s
        
        # if len(s)<2:
        #     return s
        # first=s[0]
        # remain=self.reverseString(s[1:])
        # remain.append(first)
        # return remain

        # if len(s)==1:
        #     return s
        # first=s[0]
        # res=self.reverseString(s[1:])
        # res.append(first)
        # return res

s = ["h","e","l","l","o"]
b=Solution()
b.reverseString(s)