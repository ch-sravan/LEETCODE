def mergesort(a,b,n,m,l):
    i=0
    j=0
    k=0
    while(i<n and j<m):
        if(a[i]<b[j]):
            l[k]=a[i]
            k+=1
            i+=1
        else:
            l[k]=b[j]
            k+=1
            j+=1
    while(i<n):
        l[k]=a[i]
        k+=1
        i+=1
    while(j<m):
        l[k]=b[j]
        k+=1
        j+=1
    return l
    
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        l=[]
        for i in range(n+m):
            l.append("0")
        me(nums1,nums2,m,n,l)
        for i in range(len(l)):
            nums1[i]=l[i]
