class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=max(nums)
        b=min(nums)
        r1=(a*(a+1))//2
        r2=sum(nums)
        if(a==1 and nums[0]==1 and len(nums)==1 or b==1):
            return 0
        elif(r1==r2):
            return a+1
        else:
            return r1-r2
