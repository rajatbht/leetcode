class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        total=sum(arr)
        target = total//3
        target2 = total/3
        if float(target) != target2:
            return False
        left_sum=0
        right_sum=0
        mid_sum=None
        p1=0
        p2= len(arr)-1
        while left_sum != target or right_sum != target:
            if p1 < p2:
                mid_sum = 0
                if left_sum == target:
                    pass
                else:
                    left_sum += arr[p1]
                    p1 += 1
                if right_sum == target:
                    pass
                else:
                    right_sum += arr[p2]
                    p2 -= 1
        if left_sum != right_sum:
            return False
        else:
            if p1 <= p2 and mid_sum != None:               
                while p1 <= p2:
                    mid_sum += arr[p1] + arr[p2]
                    if p1 == p2:
                        mid_sum -= arr[p1]
                    p1 += 1
                    p2 -= 1
            if left_sum == mid_sum == right_sum:
                return True
        return False
arr=[1,-1,1,-1]
a=Solution()
a.canThreePartsEqualSum(arr)