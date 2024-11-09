# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=head
        dummy.next=curr
        curr=dummy
        return_curr=curr
        length=0
        while head is not None:
            length+=1
            head=head.next
        to_remove_at=length-n+1
        if to_remove_at==0:
            return None
        i=1
        while curr is not None:
            if i==to_remove_at:
                curr.next=curr.next.next
            curr=curr.next
            i+=1
        return dummy.next
        
            
        

        