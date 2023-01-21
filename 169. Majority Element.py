class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        l1=set(nums)
        l=list(l1)
        t=[]
        for i in range(len(l)):
            a=nums.count(l[i])
            if(a>n//2):
                t.append(l[i])
        return t[0]
