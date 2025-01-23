# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l=[]
        def traverseTree(root,l):
            if root is None:
                return 0
            else:
                traverseTree(root.left,l)
                l.append(root.val)
                traverseTree(root.right,l)
        traverseTree(root,l)
        for i in range(len(l)-1):
            if l[i]<l[i+1]:
                pass
            else:
                return False
        return True


        