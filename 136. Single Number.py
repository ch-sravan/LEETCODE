class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l1=set(nums)
        l=list(l1)
        t=[]
        for i in range(len(l)):
            a=nums.count(l[i])
            if(a==1):
                t.append(l[i])
        return t[0]
