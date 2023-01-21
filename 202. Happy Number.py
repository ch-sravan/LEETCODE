class Solution(object):
    def isHappy(self, n):
        if n == 1 :
            return True
        if n < 6:
            return False
        r=0;
        for i in str(n):
            r+=int(i)*int(i);
        return self.isHappy(r)
