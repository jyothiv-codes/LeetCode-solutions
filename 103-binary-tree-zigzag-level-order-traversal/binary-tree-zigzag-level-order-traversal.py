# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer=[]
        if root is None:
            return []
        q=deque()
        q.append(root)
        reverse=False
        while q:
            n=len(q)
            temp=[]
            for i in range(n):
                node=q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if reverse:
                answer.append(temp[::-1])
                reverse=False
            else:
                answer.append(temp)
                reverse=True
        return answer

            
        
        
        