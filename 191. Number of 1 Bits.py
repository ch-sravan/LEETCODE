class Solution:
    def hammingWeight(self, n: int) -> int:
        a=list(bin(n))
        #print(a)
        #l=list(map(str,int(a)))
        return a.count("1")
