class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        start=0
        end=len(nums)-1
        while start<end:
            if nums[start] not in dict:
                dict[nums[start]]=nums[start]
                nums.pop(start)
            if nums[end] not in dict:
                dict[nums[end]]=nums[end]
                nums.pop(end)
        return len(dict)
nums=[0,0,1,1,1,2,2,3,3,4]
a=Solution()
a.removeDuplicates(nums)