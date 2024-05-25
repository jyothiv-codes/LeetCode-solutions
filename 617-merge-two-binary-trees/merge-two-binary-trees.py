# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        root=None
        curr=root
        def merge(root,root1,root2):
            if root1 and root2:
                root=TreeNode(root1.val+root2.val)
                root.left=merge(root,root1.left,root2.left)
                root.right=merge(root,root1.right,root2.right)
            if not root1:
                return root2
            if not root2:
                return root1
            return root
        curr=merge(root,root1,root2)    
        return curr
        