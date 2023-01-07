LINK:https://leetcode.com/problems/shuffle-the-array/description/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[]
        n=len(nums)//2
        l1=nums[n:]
        for i in range(n):
            l.append(nums[i])
            l.append(l1[i])
        return l
