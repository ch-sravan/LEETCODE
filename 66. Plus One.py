class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n="".join(map(str,digits))
        n1=int(n)+1
        n2=list(map(int, str(n1)))
        return n2
