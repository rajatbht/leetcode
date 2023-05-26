class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(nums)
        left_sum=0
        for i,x in enumerate(nums):
            if left_sum == total-left_sum-x:
                return i
            left_sum += x
        return -1