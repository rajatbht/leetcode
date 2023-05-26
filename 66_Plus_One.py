class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) != 0:
            last=digits.pop()
            if last == 9:
                digits = self.plusOne(digits)
                digits.append(0)
            else:
                digits.append(last+1)
            return digits
        digits.append(1)
        return digits

digits=[1,2,3,9]
a=Solution()
a.plusOne(digits)