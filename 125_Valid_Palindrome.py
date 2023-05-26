class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start=0
        end=len(s)-1
        while start<end:
            if s[start].isalnum()==False:
                start+=1
            elif s[end].isalnum()==False:
                end-=1
            elif s[start].lower()!=s[end].lower():
                c=s[start]
                d=s[end]
                return False
            else:
                start+=1
                end-=1
        return True

s = ":,"
b=Solution()
b.isPalindrome(s)