LINK:https://leetcode.com/problems/running-sum-of-1d-array/description/
    
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        a=0
        for i in range(len(nums)):
            a+=nums[i]
            l.append(a)
        return l
