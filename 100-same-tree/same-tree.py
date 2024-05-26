# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def tree(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None or p.val!=q.val:
                return False
            else:
                return tree(p.left,q.left) and tree(p.right,q.right)
            return True
        return tree(p,q)
