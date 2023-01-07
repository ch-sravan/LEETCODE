# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def len(head):
    c=0
    while(head!=None):
        c+=1
        head=head.next
    return c
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a=len(head)
        b=a-n
        t=head
        if(b==0):
            return head.next
        for i in range(b-1):
            head=head.next
        if(head.next!=None):
            head.next=head.next.next
        return t
