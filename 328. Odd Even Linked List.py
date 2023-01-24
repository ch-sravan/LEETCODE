# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def l(head):
    c=0
    while(head!=None):
        c+=1
        head=head.next
    return c
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        le=l(head)
        i=0
        l1=[]
        l2=[]
        while(head!=None):
            if(i%2==0):
                l1.append(head.val)
            else:
                l2.append(head.val)
            i+=1
            head=head.next
        print(l1)
        print(l2)
        n=ListNode(0)
        t=n
        for i in range(len(l1)):
            a=ListNode(l1[i])
            n.next=a
            n=n.next
        for i in range(len(l2)):
            a=ListNode(l2[i])
            n.next=a
            n=n.next
        return t.next
