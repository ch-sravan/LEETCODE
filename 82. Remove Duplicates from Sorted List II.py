# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        r1=[]
        while(head!=None):
            l.append(head.val)
            head=head.next
        l2=set(l)
        l1=list(l2)
        for i in range(len(l1)):
            a=l.count(l1[i])
            if(a==1):
                r1.append(l1[i])
        r=sorted(r1)
        n=ListNode(0)
        t=n
        for i in range(len(r)):
            q=ListNode(r[i])
            n.next=q
            n=n.next
        return t.next
