class Solution:
    def addDigits(self, num: int) -> int:
        n=num
        while n>9:
            l=list(map(int,str(n)))
            n=sum(l)
        return n
