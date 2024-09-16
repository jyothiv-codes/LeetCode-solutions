# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.s=0
    def subSum(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0 
        left=self.subSum(node.left)
        right=self.subSum(node.right)
        self.s+=abs(left-right)
        return node.val+left+right
            
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        print(self.subSum(root))
        return self.s
        