# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while root:
            if p.val<root.val and q.val<root.val:
                root=root.left
            elif p.val>root.val and q.val>root.val:
                root=root.right
            elif p.val<root.val and q.val>root.val:
                return root
            elif p.val>root.val and q.val<root.val:
                return root
            elif p.val==root.val and q.val>root.val:
                return p
            elif q.val==root.val and p.val<root.val:
                return q
            elif p.val==root.val and q.val<root.val:
                return p
            elif q.val==root.val and p.val>root.val:
                return q


        