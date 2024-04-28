# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue=[]
        final_ans=[]
        temp=[]
        if root is None:
            return final_ans
        queue.append(root)
        while len(queue)>0:
            n=len(queue)
            temp=[]
            for i in range(n):
                curr=queue.pop(0)
                temp.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            if len(temp)>0:
                final_ans.append(temp)
        return final_ans
        
            
                


            
