class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        a=list(d.keys())
        b=list(d.values())
        s=-1
        ma=-1
        for i in range(len(a)):
            if(a[i]==b[i]):
                s=b[i]
            ma=max(s,ma)
        return ma
