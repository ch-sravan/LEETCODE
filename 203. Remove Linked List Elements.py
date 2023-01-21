# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        t=head
        if(head==None):
            return head
        if(head.val==val and head.next==None):
            return 
        while(head!=None and head.next!=None):
            if(head.next.val==val):
                head.next=head.next.next
            else:
                head=head.next
            if(t.val==val):
                t=t.next
        return t
