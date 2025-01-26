# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s=""
        l=[]
        def calcSum(root,s,l):
            if root is None:
                l.append(s)
            s+=str(root.val)
            print("s",s)
            if root.left is None and root.right is None:
                l.append(s)
            if root.left:
                calcSum(root.left,s,l)
            if root.right:
                calcSum(root.right,s,l)
        calcSum(root,s,l)
        print(l)
        sum_=0
        for x in l:
            sum_+=int(x)
        return sum_

        