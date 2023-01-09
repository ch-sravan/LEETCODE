class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            a=nums[i]
            if(nums.count(a)==1):
                s+=a
        return s
