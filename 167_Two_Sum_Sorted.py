class Solution(object):
    def twoSum(self, numbers, target):
        index1=0
        index2=len(numbers)-1
        while numbers[index1] + numbers[index2] != target:
            if target < numbers[index1] + numbers[index2]:
                index2-=1
            else:
                index1+=1
        return [index1 + 1 , index2 + 1]