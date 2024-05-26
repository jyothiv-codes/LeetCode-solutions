# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        val=root.val
        def tree(root,val):
            if root is None or root.val==None:
                return True
            if root.val!=val:
                return False
                
            else:
                return tree(root.left,val) and tree(root.right,val)
            return False
                
        return tree(root,val)
        