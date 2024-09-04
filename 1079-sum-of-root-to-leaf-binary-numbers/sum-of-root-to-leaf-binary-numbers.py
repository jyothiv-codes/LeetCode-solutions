# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        binary=[]
        if root.left is None and root.right is None:
            return root.val
        def leafTraverse(root,binary,curr_sum):
            if root is None:
                return
            if root.left is None and root.right is None:
                binary.append(curr_sum+str(root.val))
                return

            else:
                leafTraverse(root.left,binary,curr_sum+str(root.val))  
                leafTraverse(root.right,binary,curr_sum+str(root.val))
                
                    
        leafTraverse(root,binary,"")
        print(binary)
        sum_=0
        for i in range(len(binary)):
            
            sum_+=int(binary[i],2)
        return sum_
        


        