# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer=[]
        if root is None:
            return []
        queue=[root]
        reverse=False
        while len(queue)>0:
            n=len(queue)
            temp=[]
            for i in range(n):
                node=queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp.append(node.val)
            if reverse:
                answer.append(temp[::-1])
                reverse=False
            else:
                reverse=True
                answer.append(temp)
        return answer
            
        