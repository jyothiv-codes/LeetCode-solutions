# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(root1,root2):
            if root1 and not root2:
                return False
            if root1 is None and root2 is None:
                return True
            if not root1 and root2:
                return False
            if root1 and root2 and (root1.val!=root2.val):
                return False
            if not symmetric(root1.left,root2.right):
                return False
            if not symmetric(root2.left,root1.right):
                return False
            return True
        return symmetric(root.left,root.right)


            


        