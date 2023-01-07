# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i=list1
        j=list2
        if(list1==None):
            return list2
        if(list2==None):
            return list1
        n=ListNode(0)
        t=n
        while (i!=None and j!=None):
            if(i.val<=j.val):
                n.next=i
                i=i.next
            else:
                n.next=j
                j=j.next
            n=n.next
        if(i!=None):
            n.next=i
        else:
            n.next=j
        return t.next
