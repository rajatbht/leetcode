class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1:
            return n
        i=1
        count=0
        while n!=count:
            item=i
            for prime in 2,3,5:
                while item%prime==0:
                    item= item // prime
            if item==1:
                i+=1
                count+=1
            else:
                i+=1
        return i-1

n=7
b=Solution()
b.nthUglyNumber(n)