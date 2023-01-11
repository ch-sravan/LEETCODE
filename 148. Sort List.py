# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=ListNode(0)
        t=n
        l1=[]
        while(head!=None):
            l1.append(head.val)
            head=head.next
        l=sorted(l1)
        for i in range(len(l)):
            n1=ListNode(l[i])
            n.next=n1
            n=n.next
        return t.next
