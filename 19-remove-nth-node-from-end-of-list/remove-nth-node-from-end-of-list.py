# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length=0
        curr=head
        curr2=head
        to_return=head
        while curr is not None:
            curr=curr.next
            length+=1
        if length==1 and n==1:
            return None
        
        to_remove=length-n
        i=1

        if n==1 and length==1:
            return None
        if n==length:
            return head.next
        while i<to_remove:
            curr2=curr2.next
            i+=1
        curr2.next=curr2.next.next
        return to_return
        