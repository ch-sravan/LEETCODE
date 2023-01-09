class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l=list(s)
        l1=[]
        for i in range(len(l)):
            l1.append(" ")
        for i in range(len(l)):
            l1[indices[i]]=l[i]
        r="".join(l1)
        return r
