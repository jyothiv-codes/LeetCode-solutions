# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        visited=[]
        while curr is not None:
            if curr in visited:
                return True
            visited.append(curr)
            curr=curr.next
        return False
        