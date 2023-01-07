class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        r=nums1+nums2
        s=sorted(r)
        a=0
        b=len(s)-1
        c=(a+b)//2
        if len(s)%2==1:
            return s[c]
        else:
            return (s[c]+s[c+1])/2
