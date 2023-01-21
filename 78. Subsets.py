class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[]
        n=2**len(nums)
        for i in range(n):
            r=[]
            for j in range(len(nums)):
                if(i&(1<<j)):
                    r.append(nums[j])
            l.append(r)
        return l
