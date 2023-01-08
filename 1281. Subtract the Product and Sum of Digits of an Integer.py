class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=list(map(int,str(n)))
        c=1
        for i in range(len(l)):
            c=c*l[i]
        return c-sum(l)
