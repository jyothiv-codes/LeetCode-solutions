# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        max_=[]
        def traversal(max_,root):
            if root is None:
                return 
            if root.val not in max_:
                max_.append(root.val)
            traversal(max_,root.left)
            traversal(max_,root.right)
        traversal(max_,root)
        max_.sort()
        print(max_)
        if len(max_)==1:
            return -1
        return max_[1]

            
            
        
        
        