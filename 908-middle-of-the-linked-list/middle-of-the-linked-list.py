# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n=0 #length of the linked list
        curr=head
        while curr is not None:
            curr=curr.next
            n+=1
        print("length of the linked list",n)
        proc=0
        curr_proc=head
        print("curr_proc",curr_proc)
        while proc<(n/2):
            curr_proc=curr_proc.next
            proc+=1
        return curr_proc
        
        