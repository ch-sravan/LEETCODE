# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def rev(head):
    p=None
    while(head!=None):
        t=head.next
        head.next=p
        p=head
        head=t
    return p

def mid(head):
    s=head
    f=head
    while(f.next!=None and f.next.next!=None):
        s=s.next
        f=f.next.next
    return s
def res(a,c):
    t=a
    while(a!=None and c!=None):
        t1=a.next
        t2=c.next
        a.next=c
        c.next=t1
        a=t1
        c=t2
    return t
    
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        a=mid(head)
        b=a.next
        a.next=None
        c=rev(b)
        return res(head,c)
