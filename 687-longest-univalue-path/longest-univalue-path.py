# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        l=[0]
        if root is None:
            return 0
        def solve(root,parent,l):
            if root is None:
                return 0
            left=solve(root.left,root.val,l)
            right=solve(root.right,root.val,l)
            l[0]=max(l[0],left+right)
            print("curr,ans,",root.val,parent,l)
            if root.val==parent:
                return max(left,right)+1
            else:
                return 0
        ans=0
        solve(root,-1,l)
        return l[0]

        