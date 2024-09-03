# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        minimum=[]
        def minTraverse(minimum,root,curr):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                minimum.append(curr+1)
                return
            else:
                return minTraverse(minimum,root.left,1+curr) or minTraverse(minimum,root.right,1+curr)
        minTraverse(minimum,root,0)
        print(minimum)
        return min(minimum)
        