class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        no=0
        for i,n in enumerate(nums):
            no += pow(2, len(nums)-1-i) * n
            nums[i] = True if no % 5 == 0 else False
        return nums

nums=[0,1,1]
a=Solution()
a.prefixesDivBy5(nums)