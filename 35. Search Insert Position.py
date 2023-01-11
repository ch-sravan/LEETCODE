class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(target in nums):
            i=nums.index(target)
            return i
        else:
            nums.append(target)
            a=sorted(nums)
            i=a.index(target)
            return i
