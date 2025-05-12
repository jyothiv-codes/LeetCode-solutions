# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        nodes=[]
        while curr!=None and curr not in nodes:
            nodes.append(curr)
            curr=curr.next
            
        if curr in nodes:
            #print(curr.val)
            return curr
        return None
        