# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        q=deque([root])
        c=0
        while q:
            node=q.popleft()
            if node.left:
                if c:
                    return False
                q.append(node.left)
            else:
                c+=1
            if node.right:
                if c:
                    return False
                q.append(node.right)
            else:
                c+=1
        return True


        