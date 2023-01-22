class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=len(nums)
        l=set(nums)
        b=len(l)
        return b<=a-1
