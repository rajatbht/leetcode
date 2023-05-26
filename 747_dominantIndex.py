class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest=-1
        second_largest=-1
        maxIndex=0
        for i,n in enumerate(nums):
            if n>largest:
                second_largest=largest
                largest=n
                maxIndex=i
            elif n>second_largest:
                second_largest=n
        if largest<second_largest*2:
            return -1
        return maxIndex
        

nums=[0,0,0,1]
a=Solution()
a.dominantIndex(nums)