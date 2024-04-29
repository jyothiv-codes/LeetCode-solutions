# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def calc(node):
            if node is None:
                return 0
            left,right=0,0
            if node.left is not None:
                left=calc(node.left)
            if node.right is not None:
                right=calc(node.right)
            if left<0 or right<0:
                return -1
            if abs(left-right)>1:
                return -1
            return max(left,right)+1
        
        return calc(root) > -1

        