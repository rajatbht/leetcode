class Solution(object):
    def twoSum(self, nums, target):
        check={}
        for i in range(len(nums)):
            if nums[i] in check:
                return [ check[nums[i] ] , i]
            else:
                check[ target - nums[i] ] = i


        # index=0
        # while index<len(nums)-1:
        #     for i in range(index+1,len(nums)):
        #         if nums[index]+nums[i]==target:
        #             return [index,i]
        #     index+=1

            
            
