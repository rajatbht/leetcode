class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        p1 = 0
        p2 = len(strs)-1
        common_prefix =""
        for ltr in strs[p1]:
            if ltr in strs[p2]:
                common_prefix += ltr
            else:
                break
        p1 += 1
        p2 -= 1            
        while p1 <= p2:
            if common_prefix in strs[p1] and strs[p2]:
                p1 += 1
                p2 -= 1
            break
        return common_prefix

strs=["aa","ab"]
a=Solution()
a.longestCommonPrefix(strs)