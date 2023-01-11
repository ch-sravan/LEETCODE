class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=[-1,-1]
        e=nums.count(target)
        r=[]
        if(len(nums)==0 or e==0):
            return a
        else:
            d=nums.index(target)
            c=e+d-1
            r.append(d)
            r.append(c)
            return r
