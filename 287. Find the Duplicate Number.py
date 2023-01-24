class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        a=0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                a=nums[i]
        return a
