# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n=0
        # First we find the length of the linkedin list
        curr1=head
        while curr1!=None:
            n+=1
            curr1=curr1.next
        i=0
        # Traverse half of the linked list and reverse the second half
        curr2=head
        while i<int(n/2):
            curr2=curr2.next
            i+=1
        prev=None
        cur=curr2
        while cur!=None:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        # prev is the new head
        curr3=head
        m=0
        while prev!=None:
            m=max(curr3.val+prev.val,m)
            curr3=curr3.next
            prev=prev.next
        return m
            

        